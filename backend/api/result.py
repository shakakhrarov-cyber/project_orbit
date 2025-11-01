from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import get_db, Session as DBSession, MatchReport, Archetype
from pydantic import BaseModel
from typing import Optional
import numpy as np
from core.matching_engine import compute_cosine_similarity, rank_matches

router = APIRouter(prefix="/session", tags=["result"])

class MatchRecommendation(BaseModel):
    rank: int
    archetype_id: str
    name: str
    fit_score: float
    explanation: str

class ResultResponse(BaseModel):
    session_id: str
    recommendations: list[MatchRecommendation]
    confidence: Optional[float] = None
    average_uncertainty: Optional[float] = None
    questions_answered: int

@router.get("/{session_id}/result", response_model=ResultResponse)
async def get_result(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Get match recommendations for a completed session"""
    # Get session
    session = db.query(DBSession).filter(DBSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if session.status != "completed":
        raise HTTPException(status_code=400, detail="Session not completed")
    
    # Check if match report already exists
    match_report = db.query(MatchReport).filter(MatchReport.session_id == session.id).first()
    
    if match_report:
        # Return cached results
        return {
            "session_id": str(session.id),
            "recommendations": match_report.recommendations,
            "confidence": float(match_report.confidence) if match_report.confidence else None,
            "average_uncertainty": float(match_report.average_uncertainty) if match_report.average_uncertainty else None,
            "questions_answered": len(session.answered_qids)
        }
    
    # Compute user vector (simple average for MVP - will use Bayesian in Sprint 03)
    # For now, create a simple vector based on responses
    # This is a placeholder - in Sprint 03, we'll use the actual state_vector
    user_vector = np.array([0.5] * 10)  # Default vector
    
    # Get all archetypes
    archetypes = db.query(Archetype).all()
    
    if not archetypes:
        raise HTTPException(status_code=500, detail="No archetypes available")
    
    # Compute matches
    matches = rank_matches(user_vector, archetypes)
    
    # Create recommendations
    recommendations = []
    for i, match in enumerate(matches[:3], 1):
        recommendations.append({
            "rank": i,
            "archetype_id": match["archetype_id"],
            "name": match["name"],
            "fit_score": match["fit_score"],
            "explanation": match["explanation"]
        })
    
    # Save match report
    match_report = MatchReport(
        session_id=session.id,
        recommendations=recommendations,
        confidence=None,  # Will be computed in Sprint 03
        average_uncertainty=None  # Will be computed in Sprint 03
    )
    db.add(match_report)
    db.commit()
    
    return {
        "session_id": str(session.id),
        "recommendations": recommendations,
        "confidence": None,
        "average_uncertainty": None,
        "questions_answered": len(session.answered_qids)
    }

