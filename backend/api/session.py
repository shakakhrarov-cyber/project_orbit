from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import get_db, Session as DBSession, Question, User
import re
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter(prefix="/session", tags=["session"])

class QuestionResponse(BaseModel):
    id: str
    text: str
    type: str
    options: Optional[list] = None

class SessionStartResponse(BaseModel):
    session_id: str
    question: QuestionResponse

@router.post("/start", response_model=SessionStartResponse)
async def start_session(db: Session = Depends(get_db)):
    """Start a new interview session and return the first question"""
    # Create a new user (anonymous)
    user = User()
    db.add(user)
    db.flush()
    
    # Create a new session
    session = DBSession(
        user_id=user.id,
        answered_qids=[],
        status="active"
    )
    db.add(session)
    db.flush()
    
    # Get first question (static flow - ordered by numeric part of ID)
    # Extract numeric part from ID (e.g., "qid_1" -> 1) for proper ordering
    all_questions = db.query(Question).all()
    # Sort by extracting numeric part from ID
    all_questions.sort(key=lambda q: int(re.search(r'\d+', q.id).group()) if re.search(r'\d+', q.id) else 999)
    first_question = all_questions[0] if all_questions else None
    
    if not first_question:
        raise HTTPException(status_code=500, detail="No questions available in database")
    
    db.commit()
    
    return {
        "session_id": str(session.id),
        "question": {
            "id": first_question.id,
            "text": first_question.text,
            "type": first_question.type,
            "options": first_question.options
        }
    }

