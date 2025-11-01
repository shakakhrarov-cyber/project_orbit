# API Specification - ORBIT Project

RESTful API endpoints for the ORBIT adaptive interview system. All endpoints return JSON responses.

**Base URL**: `http://localhost:8000` (development)  
**API Version**: v1  
**Content-Type**: `application/json`

---

## Authentication

**Note**: No authentication required for MVP (Sprint 01-06). Admin endpoints (Sprint 07+) will require JWT authentication.

---

## Endpoints

### Session Management

#### POST /session/start

Start a new interview session and receive the first question.

**Request**:
```json
{}
```

**Response** (200 OK):
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "question": {
    "id": "qid_1",
    "text": "How do you prefer to spend your free time?",
    "type": "multiple_choice",
    "options": ["Alone", "With a small group", "In large gatherings"]
  }
}
```

**Error Responses**:
- `500 Internal Server Error`: Database error, question bank empty

**Notes**:
- Creates new session in database
- Caches session state in Redis
- Returns first question from question bank (static flow in Sprint 01, adaptive in Sprint 03+)

---

#### POST /response

Submit a response to a question and receive the next question (or done flag).

**Request**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "question_id": "qid_1",
  "answer": "Alone"
}
```

**Response - Next Question** (200 OK):
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

**Response - Session Complete** (200 OK):
```json
{
  "done": true,
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "reason": "question_limit" // or "time_limit" or "uncertainty_threshold"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid session_id, question_id, or answer format
- `404 Not Found`: Session not found
- `500 Internal Server Error`: Database error, update failure

**Notes**:
- Updates session state (answered_qids array)
- Updates parameter vector (Sprint 03+)
- Returns next question based on flow (static in Sprint 01, adaptive in Sprint 03+)
- Terminates session if: 40 questions answered, 20 minutes elapsed, or uncertainty < 0.12 (Sprint 03+)

---

### Results

#### GET /session/{session_id}/result

Retrieve match recommendations for a completed session.

**Path Parameters**:
- `session_id` (UUID): Session identifier

**Response** (200 OK):
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "recommendations": [
    {
      "rank": 1,
      "archetype_id": "archetype_1",
      "name": "Pottery Class",
      "fit_score": 0.88,
      "explanation": "Matches creative drive (0.8), low social need (0.2), tactile learning (0.9)"
    },
    {
      "rank": 2,
      "archetype_id": "archetype_2",
      "name": "Trail Running Group",
      "fit_score": 0.84,
      "explanation": "Combines moderate physical challenge and structured routine"
    },
    {
      "rank": 3,
      "archetype_id": "archetype_3",
      "name": "Photography Walks",
      "fit_score": 0.80,
      "explanation": "Balanced novelty and cognitive engagement"
    }
  ],
  "confidence": 0.85,
  "average_uncertainty": 0.10,
  "questions_answered": 22
}
```

**Error Responses**:
- `404 Not Found`: Session not found or not completed
- `500 Internal Server Error`: Matching computation error

**Notes**:
- Computes cosine similarity between user vector and all archetypes
- Returns top 3 matches ranked by fit score
- Includes confidence and uncertainty metrics (Sprint 03+)
- Results are cached in MatchReport table

---

### Admin Endpoints (Sprint 07+)

**Note**: These endpoints require JWT authentication (not implemented in Sprint 01).

#### GET /admin/questions

List all questions in the question bank.

**Query Parameters**:
- `page` (integer, optional): Page number (default: 1)
- `per_page` (integer, optional): Items per page (default: 20)
- `type` (string, optional): Filter by question type
- `locale` (string, optional): Filter by locale

**Response** (200 OK):
```json
{
  "questions": [
    {
      "id": "qid_1",
      "text": "How do you prefer to spend your free time?",
      "type": "multiple_choice",
      "targets": [0, 1],
      "created_at": "2025-01-27T10:00:00Z"
    }
  ],
  "total": 20,
  "page": 1,
  "per_page": 20
}
```

---

#### POST /admin/questions

Create a new question.

**Request**:
```json
{
  "id": "qid_21",
  "text": "Do you prefer structured or flexible schedules?",
  "type": "likert",
  "targets": [3],
  "info_weight": [0.8],
  "difficulty": 1.0,
  "locale": "en"
}
```

**Response** (201 Created):
```json
{
  "id": "qid_21",
  "text": "Do you prefer structured or flexible schedules?",
  "type": "likert",
  "targets": [3],
  "info_weight": [0.8],
  "difficulty": 1.0,
  "locale": "en",
  "created_at": "2025-01-27T10:30:00Z"
}
```

---

#### PUT /admin/questions/{question_id}

Update an existing question.

**Request**:
```json
{
  "text": "Updated question text",
  "targets": [0, 1, 2],
  "info_weight": [0.3, 0.5, 0.2]
}
```

**Response** (200 OK):
```json
{
  "id": "qid_1",
  "text": "Updated question text",
  "targets": [0, 1, 2],
  "info_weight": [0.3, 0.5, 0.2],
  "updated_at": "2025-01-27T10:35:00Z"
}
```

---

#### DELETE /admin/questions/{question_id}

Delete a question (soft delete).

**Response** (200 OK):
```json
{
  "id": "qid_1",
  "deleted": true
}
```

---

#### GET /admin/archetypes

List all archetypes.

**Response** (200 OK):
```json
{
  "archetypes": [
    {
      "id": "archetype_1",
      "name": "Pottery Class",
      "vector": [0.2, 0.4, 0.9, 0.6, 0.5, 0.7, 0.8, 0.5, 0.6, 0.3],
      "created_at": "2025-01-27T10:00:00Z"
    }
  ],
  "total": 5
}
```

---

#### POST /admin/archetypes

Create a new archetype.

**Request**:
```json
{
  "id": "archetype_6",
  "name": "Book Club",
  "vector": [0.8, 0.2, 0.7, 0.6, 0.4, 0.9, 0.3, 0.5, 0.7, 0.2],
  "min_requirements": {"0": 0.6},
  "contraindications": {},
  "resources": {
    "description": "Local book clubs and reading groups",
    "links": []
  }
}
```

**Response** (201 Created):
```json
{
  "id": "archetype_6",
  "name": "Book Club",
  "vector": [0.8, 0.2, 0.7, 0.6, 0.4, 0.9, 0.3, 0.5, 0.7, 0.2],
  "created_at": "2025-01-27T10:40:00Z"
}
```

---

#### PUT /admin/archetypes/{archetype_id}

Update an existing archetype.

**Request**:
```json
{
  "vector": [0.8, 0.3, 0.7, 0.6, 0.4, 0.9, 0.3, 0.5, 0.7, 0.2]
}
```

**Response** (200 OK):
```json
{
  "id": "archetype_6",
  "vector": [0.8, 0.3, 0.7, 0.6, 0.4, 0.9, 0.3, 0.5, 0.7, 0.2],
  "updated_at": "2025-01-27T10:45:00Z"
}
```

---

#### DELETE /admin/archetypes/{archetype_id}

Delete an archetype.

**Response** (200 OK):
```json
{
  "id": "archetype_6",
  "deleted": true
}
```

---

## Error Response Format

All error responses follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  }
}
```

**Common Error Codes**:
- `VALIDATION_ERROR`: Invalid request format
- `SESSION_NOT_FOUND`: Session ID not found
- `QUESTION_NOT_FOUND`: Question ID not found
- `SESSION_COMPLETED`: Session already completed
- `INTERNAL_ERROR`: Server error

---

## Rate Limiting

**Note**: Rate limiting not implemented in MVP. Will be added in Phase 2.

**Planned Limits**:
- `/session/start`: 10 requests/minute per IP
- `/response`: 60 requests/minute per session
- `/result`: 10 requests/minute per session

---

## Postman Collection

A Postman collection is available at `docs/postman_collection.json` (to be created).

**Collection includes**:
- Session start
- Response submission (multiple examples)
- Result retrieval
- Admin endpoints (Sprint 07+)

---

*Last Updated: 2025-01-27*

