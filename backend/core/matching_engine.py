import numpy as np
from typing import List, Dict

def compute_cosine_similarity(user_vector: np.ndarray, archetype_vector: np.ndarray) -> float:
    """Compute cosine similarity between user vector and archetype vector"""
    dot_product = np.dot(user_vector, archetype_vector)
    norm_user = np.linalg.norm(user_vector)
    norm_archetype = np.linalg.norm(archetype_vector)
    
    if norm_user == 0 or norm_archetype == 0:
        return 0.0
    
    similarity = dot_product / (norm_user * norm_archetype)
    return float(similarity)

def generate_explanation(archetype_name: str, user_vector: np.ndarray, archetype_vector: np.ndarray) -> str:
    """Generate explanation for match (simple version for MVP)"""
    # Find top 3 matched parameters
    differences = np.abs(user_vector - archetype_vector)
    top_indices = np.argsort(differences)[:3]
    
    param_names = [
        "social preference",
        "physical intensity",
        "creative drive",
        "structure preference",
        "cost sensitivity",
        "schedule regularity",
        "learning style",
        "novelty appetite",
        "motivation type",
        "access constraints"
    ]
    
    explanations = []
    for idx in top_indices:
        param_name = param_names[idx]
        user_val = user_vector[idx]
        arch_val = archetype_vector[idx]
        
        if abs(user_val - arch_val) < 0.2:
            explanations.append(f"{param_name} ({arch_val:.1f})")
    
    if explanations:
        return f"Matches {', '.join(explanations)}"
    else:
        return f"Matches your preferences for {archetype_name.lower()}"

def rank_matches(user_vector: np.ndarray, archetypes: List) -> List[Dict]:
    """Rank archetypes by cosine similarity"""
    matches = []
    
    for archetype in archetypes:
        archetype_vector = np.array(archetype.vector)
        fit_score = compute_cosine_similarity(user_vector, archetype_vector)
        
        explanation = generate_explanation(archetype.name, user_vector, archetype_vector)
        
        matches.append({
            "archetype_id": archetype.id,
            "name": archetype.name,
            "fit_score": fit_score,
            "explanation": explanation
        })
    
    # Sort by fit_score descending
    matches.sort(key=lambda x: x["fit_score"], reverse=True)
    
    return matches

