from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import get_db, Session as DBSession, Question, Response
import re
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

router = APIRouter(prefix="/response", tags=["response"])

class ResponseRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str | int | float

class QuestionResponse(BaseModel):
    id: str
    text: str
    type: str
    options: Optional[list] = None

class ResponseResponse(BaseModel):
    question: Optional[QuestionResponse] = None
    done: Optional[bool] = None
    session_id: Optional[str] = None
    reason: Optional[str] = None

@router.post("", response_model=ResponseResponse)
async def submit_response(
    request: ResponseRequest,
    db: Session = Depends(get_db)
):
    """Submit a response and get the next question"""
    # Get session
    try:
        session = db.query(DBSession).filter(DBSession.id == request.session_id).first()
    except Exception:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if session.status == "completed":
        raise HTTPException(status_code=400, detail="Session already completed")
    
    # Check time limit (20 minutes)
    if session.created_at + timedelta(minutes=20) < datetime.utcnow():
        session.status = "completed"
        session.completed_at = datetime.utcnow()
        db.commit()
        return {
            "done": True,
            "session_id": str(session.id),
            "reason": "time_limit"
        }
    
    # Get question
    question = db.query(Question).filter(Question.id == request.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Save response
    response = Response(
        session_id=session.id,
        question_id=question.id,
        payload={
            "answer": request.answer,
            "normalized_value": None  # Will be computed in Sprint 03
        }
    )
    db.add(response)
    
    # Update session - must reassign to trigger SQLAlchemy change detection for JSONB
    if question.id not in session.answered_qids:
        session.answered_qids = session.answered_qids + [question.id]  # Creates new list
    session.updated_at = datetime.utcnow()
    
    # Check question limit (40 questions)
    if len(session.answered_qids) >= 40:
        session.status = "completed"
        session.completed_at = datetime.utcnow()
        db.commit()
        return {
            "done": True,
            "session_id": str(session.id),
            "reason": "question_limit"
        }
    
    # Get next question (static flow - sequential, ordered by numeric part of ID)
    # Extract numeric part from ID (e.g., "qid_1" -> 1) for proper ordering
    all_questions = db.query(Question).all()
    # Sort by extracting numeric part from ID
    all_questions.sort(key=lambda q: int(re.search(r'\d+', q.id).group()) if re.search(r'\d+', q.id) else 999)
    answered_ids = set(session.answered_qids)
    next_question = None
    
    for q in all_questions:
        if q.id not in answered_ids:
            next_question = q
            break
    
    if not next_question:
        # No more questions
        session.status = "completed"
        session.completed_at = datetime.utcnow()
        db.commit()
        return {
            "done": True,
            "session_id": str(session.id),
            "reason": "no_more_questions"
        }
    
    db.commit()
    
    return {
        "question": {
            "id": next_question.id,
            "text": next_question.text,
            "type": next_question.type,
            "options": next_question.options
        }
    }

