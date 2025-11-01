import json
import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from models import Question, Archetype, get_db
from config import settings

def seed_questions(db: Session):
    """Seed questions from JSON file"""
    # Get the script directory
    script_dir = Path(__file__).parent.parent
    questions_path = script_dir / "seed_data" / "questions.json"
    
    with open(questions_path, "r") as f:
        questions_data = json.load(f)
    
    for q_data in questions_data:
        # Check if question already exists
        existing = db.query(Question).filter(Question.id == q_data["id"]).first()
        if existing:
            continue
        
        question = Question(
            id=q_data["id"],
            text=q_data["text"],
            type=q_data["type"],
            options=q_data.get("options"),
            targets=q_data.get("targets"),
            info_weight=q_data.get("info_weight"),
            difficulty=str(q_data.get("difficulty", "1.0")),
            locale=q_data.get("locale", "en")
        )
        db.add(question)
    
    db.commit()
    print(f"Seeded {len(questions_data)} questions")

def seed_archetypes(db: Session):
    """Seed archetypes from JSON file"""
    # Get the script directory
    script_dir = Path(__file__).parent.parent
    archetypes_path = script_dir / "seed_data" / "archetypes.json"
    
    with open(archetypes_path, "r") as f:
        archetypes_data = json.load(f)
    
    for a_data in archetypes_data:
        # Check if archetype already exists
        existing = db.query(Archetype).filter(Archetype.id == a_data["id"]).first()
        if existing:
            continue
        
        archetype = Archetype(
            id=a_data["id"],
            name=a_data["name"],
            vector=a_data["vector"],
            min_requirements=a_data.get("min_requirements"),
            contraindications=a_data.get("contraindications"),
            resources=a_data.get("resources")
        )
        db.add(archetype)
    
    db.commit()
    print(f"Seeded {len(archetypes_data)} archetypes")

if __name__ == "__main__":
    db = next(get_db())
    seed_questions(db)
    seed_archetypes(db)
    print("Seeding complete!")
