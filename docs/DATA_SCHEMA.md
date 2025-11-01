# Data Schema - ORBIT Project

JSON schemas for all entities in the ORBIT system. These schemas define the structure of data stored in PostgreSQL (with JSONB fields) and used in API requests/responses.

---

## User

```json
{
  "id": "uuid",
  "created_at": "2025-01-27T10:00:00Z",
  "email": "optional_email@example.com"
}
```

**Database Table**: `users`
- `id`: UUID, primary key
- `created_at`: timestamp, not null
- `email`: varchar(255), nullable (optional, collected after results)

---

## Session

```json
{
  "id": "uuid",
  "user_id": "uuid",
  "state_vector": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
  "covariance": [[0.0625, 0, ...], [0, 0.0625, ...], ...],
  "answered_qids": ["qid_1", "qid_2", ...],
  "status": "active | completed | abandoned",
  "created_at": "2025-01-27T10:00:00Z",
  "updated_at": "2025-01-27T10:15:00Z",
  "completed_at": "2025-01-27T10:15:00Z | null"
}
```

**Database Table**: `sessions`
- `id`: UUID, primary key
- `user_id`: UUID, foreign key → users.id
- `state_vector`: JSONB, array of 10 floats (0-1), nullable (null initially, set after first response)
- `covariance`: JSONB, 10x10 matrix of floats, nullable (null initially)
- `answered_qids`: JSONB, array of strings (question IDs)
- `status`: varchar(20), default 'active'
- `created_at`: timestamp, not null
- `updated_at`: timestamp, not null
- `completed_at`: timestamp, nullable

**Notes**:
- `state_vector`: 10-dimensional parameter vector, initialized to [0.5]*10 ± 0.25 variance (Sprint 03+)
- `covariance`: 10x10 covariance matrix for uncertainty tracking (Sprint 03+)
- `answered_qids`: Tracks which questions have been answered (prevents duplicates)

---

## Question

```json
{
  "id": "qid_1",
  "text": "How do you prefer to spend your free time?",
  "type": "multiple_choice | likert | slider | free_text",
  "options": ["Option A", "Option B", "Option C"],
  "targets": [0, 1, 2],
  "info_weight": [0.3, 0.5, 0.2],
  "difficulty": 1.0,
  "locale": "en",
  "created_at": "2025-01-27T10:00:00Z",
  "updated_at": "2025-01-27T10:00:00Z"
}
```

**Database Table**: `questions`
- `id`: varchar(50), primary key (e.g., "qid_1")
- `text`: text, not null
- `type`: varchar(20), not null (multiple_choice, likert, slider, free_text)
- `options`: JSONB, array of strings (for multiple-choice), nullable
- `targets`: JSONB, array of integers (parameter indices 0-9), nullable
- `info_weight`: JSONB, array of floats (weights for each target), nullable
- `difficulty`: float, default 1.0 (used for fatigue constraint)
- `locale`: varchar(10), default 'en'
- `created_at`: timestamp, not null
- `updated_at`: timestamp, not null

**Notes**:
- `targets`: Which parameters this question targets (e.g., [0, 1] targets Social Mode and Physical Intensity)
- `info_weight`: Weight for each target (higher = more informative for that parameter)
- `type`: Question type determines response format
  - `multiple_choice`: Select one option
  - `likert`: 1-5 scale
  - `slider`: Continuous 0-1 value
  - `free_text`: Open-ended text (Sprint 19+)

---

## Response

```json
{
  "id": "uuid",
  "session_id": "uuid",
  "question_id": "qid_1",
  "payload": {
    "answer": "Option A",
    "normalized_value": 0.0
  },
  "latency_ms": 2500,
  "timestamp": "2025-01-27T10:05:00Z"
}
```

**Database Table**: `responses`
- `id`: UUID, primary key
- `session_id`: UUID, foreign key → sessions.id
- `question_id`: varchar(50), foreign key → questions.id
- `payload`: JSONB, question-specific answer data
- `latency_ms`: integer, time taken to answer (milliseconds)
- `timestamp`: timestamp, not null

**Payload Examples**:
- **Multiple Choice**: `{"answer": "Option A", "normalized_value": 0.0}`
- **Likert**: `{"answer": 4, "normalized_value": 0.75}` (4/5 scale → 0.75)
- **Slider**: `{"answer": 0.65, "normalized_value": 0.65}`
- **Free Text**: `{"answer": "I enjoy creative activities", "normalized_value": null}` (Sprint 19+)

---

## Archetype

```json
{
  "id": "archetype_1",
  "name": "Pottery Class",
  "vector": [0.2, 0.4, 0.9, 0.6, 0.5, 0.7, 0.8, 0.5, 0.6, 0.3],
  "min_requirements": {"0": 0.1, "3": 0.5},
  "contraindications": {"1": [0.8, 0.9, 1.0]},
  "resources": {
    "description": "Local pottery studios and classes",
    "links": ["https://example.com/pottery-studio-1"]
  },
  "created_at": "2025-01-27T10:00:00Z",
  "updated_at": "2025-01-27T10:00:00Z"
}
```

**Database Table**: `archetypes`
- `id`: varchar(50), primary key (e.g., "archetype_1")
- `name`: varchar(255), not null
- `vector`: JSONB, array of 10 floats (0-1), not null (ideal parameter values)
- `min_requirements`: JSONB, object mapping parameter index to minimum value, nullable
- `contraindications`: JSONB, object mapping parameter index to disallowed values, nullable
- `resources`: JSONB, object with description and links, nullable
- `created_at`: timestamp, not null
- `updated_at`: timestamp, not null

**Notes**:
- `vector`: 10-dimensional parameter vector representing ideal user profile
- `min_requirements`: Hard thresholds (e.g., parameter 0 must be >= 0.1)
- `contraindications`: Values that disqualify match (e.g., parameter 1 cannot be 0.8-1.0)
- `resources`: Links to real opportunities (Sprint 25+)

**Parameter Mapping**:
- 0: Social Mode (0 = solo, 1 = group)
- 1: Physical Intensity (0 = low, 1 = high)
- 2: Cognitive/Creative Drive (0 = low, 1 = high)
- 3: Structure Preference (0 = self-guided, 1 = scheduled)
- 4: Cost Sensitivity (0 = low, 1 = high)
- 5: Schedule Regularity (0 = irregular, 1 = regular)
- 6: Learning Style (0 = kinesthetic, 1 = visual/auditory)
- 7: Novelty Appetite (0 = comfort zone, 1 = experimental)
- 8: Motivation Type (0 = competition, 1 = mastery/relaxation)
- 9: Access Constraints (0 = none, 1 = high constraints)

---

## MatchReport

```json
{
  "id": "uuid",
  "session_id": "uuid",
  "recommendations": [
    {
      "rank": 1,
      "archetype_id": "archetype_1",
      "archetype_name": "Pottery Class",
      "fit_score": 0.88,
      "explanation": "Matches creative drive (0.8), low social need (0.2), tactile learning (0.9)"
    },
    {
      "rank": 2,
      "archetype_id": "archetype_2",
      "archetype_name": "Trail Running Group",
      "fit_score": 0.84,
      "explanation": "Combines moderate physical challenge and structured routine"
    },
    {
      "rank": 3,
      "archetype_id": "archetype_3",
      "archetype_name": "Photography Walks",
      "fit_score": 0.80,
      "explanation": "Balanced novelty and cognitive engagement"
    }
  ],
  "confidence": 0.85,
  "average_uncertainty": 0.10,
  "created_at": "2025-01-27T10:15:00Z"
}
```

**Database Table**: `match_reports`
- `id`: UUID, primary key
- `session_id`: UUID, foreign key → sessions.id, unique
- `recommendations`: JSONB, array of match objects, not null
- `confidence`: float (0-1), nullable (Sprint 03+)
- `average_uncertainty`: float (0-1), nullable (Sprint 03+)
- `created_at`: timestamp, not null

**Notes**:
- `recommendations`: Top 3 matches with rank, name, fit score, explanation
- `confidence`: Overall confidence in recommendations (Sprint 03+)
- `average_uncertainty`: Mean uncertainty across all parameters (Sprint 03+)

---

## API Request/Response Schemas

### POST /session/start

**Request**:
```json
{}
```

**Response**:
```json
{
  "session_id": "uuid",
  "question": {
    "id": "qid_1",
    "text": "How do you prefer to spend your free time?",
    "type": "multiple_choice",
    "options": ["Option A", "Option B", "Option C"]
  }
}
```

---

### POST /response

**Request**:
```json
{
  "session_id": "uuid",
  "question_id": "qid_1",
  "answer": "Option A"
}
```

**Response** (next question):
```json
{
  "question": {
    "id": "qid_2",
    "text": "On a scale of 1-5, how important is social interaction?",
    "type": "likert",
    "options": [1, 2, 3, 4, 5]
  }
}
```

**Response** (done):
```json
{
  "done": true,
  "session_id": "uuid"
}
```

---

### GET /session/{session_id}/result

**Response**:
```json
{
  "session_id": "uuid",
  "recommendations": [
    {
      "rank": 1,
      "name": "Pottery Class",
      "fit_score": 0.88,
      "explanation": "Matches creative drive (0.8), low social need (0.2), tactile learning (0.9)"
    },
    {
      "rank": 2,
      "name": "Trail Running Group",
      "fit_score": 0.84,
      "explanation": "Combines moderate physical challenge and structured routine"
    },
    {
      "rank": 3,
      "name": "Photography Walks",
      "fit_score": 0.80,
      "explanation": "Balanced novelty and cognitive engagement"
    }
  ],
  "confidence": 0.85,
  "average_uncertainty": 0.10
}
```

---

## Validation Rules

### State Vector
- Must be array of 10 floats
- Each value must be between 0 and 1
- Default: `[0.5, 0.5, ..., 0.5]`

### Covariance Matrix
- Must be 10x10 matrix of floats
- Must be symmetric (covariance[i][j] == covariance[j][i])
- Diagonal values represent variance (must be >= 0)
- Default: `0.25² * I` (identity matrix)

### Question Targets
- Must be array of integers (0-9)
- Length must match `info_weight` length
- Each target must be valid parameter index (0-9)

### Archetype Vector
- Must be array of 10 floats
- Each value must be between 0 and 1
- Represents ideal parameter values

### Fit Score
- Must be float between 0 and 1
- Calculated as: `cosine_similarity(user_vector, archetype_vector)`
- Higher = better match

---

*Last Updated: 2025-01-27*

