from sqlalchemy import create_engine, Column, String, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    email = Column(String(255), nullable=True)

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    state_vector = Column(JSON, nullable=True)  # 10-dim array
    covariance = Column(JSON, nullable=True)  # 10x10 matrix
    answered_qids = Column(JSON, default=list, nullable=False)  # Array of question IDs
    status = Column(String(20), default="active", nullable=False)  # active, completed, abandoned
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    
    user = relationship("User", backref="sessions")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(String(50), primary_key=True)
    text = Column(String, nullable=False)
    type = Column(String(20), nullable=False)  # multiple_choice, likert, slider, free_text
    options = Column(JSON, nullable=True)  # Array of options
    targets = Column(JSON, nullable=True)  # Array of parameter indices (0-9)
    info_weight = Column(JSON, nullable=True)  # Array of weights
    difficulty = Column(String, default="1.0", nullable=False)
    locale = Column(String(10), default="en", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"), nullable=False)
    question_id = Column(String(50), ForeignKey("questions.id"), nullable=False)
    payload = Column(JSON, nullable=False)  # Answer data
    latency_ms = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    session = relationship("Session", backref="responses")
    question = relationship("Question", backref="responses")

class Archetype(Base):
    __tablename__ = "archetypes"
    
    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False)
    vector = Column(JSON, nullable=False)  # 10-dim array
    min_requirements = Column(JSON, nullable=True)  # Object mapping param index to min value
    contraindications = Column(JSON, nullable=True)  # Object mapping param index to disallowed values
    resources = Column(JSON, nullable=True)  # Object with description and links
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class MatchReport(Base):
    __tablename__ = "match_reports"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"), nullable=False, unique=True)
    recommendations = Column(JSON, nullable=False)  # Array of match objects
    confidence = Column(String, nullable=True)  # 0-1 float
    average_uncertainty = Column(String, nullable=True)  # 0-1 float
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    session = relationship("Session", backref="match_report", uselist=False)

