# Architecture Notes - ORBIT Project

## System Overview
ORBIT is a 3-layer web application that uses adaptive questioning powered by Bayesian inference to match users with hobbies or roles. The system consists of:

1. **Front-End Layer**: React SPA that displays questions conversationally
2. **Inference Layer**: FastAPI backend that adapts question flow and updates parameter vectors
3. **Data Layer**: PostgreSQL for persistence, Redis for session caching

The architecture supports incremental development: static flow first (MVP), then adaptive engine (Sprint 03+).

---

## Technology Stack

### Frontend
- **Framework**: React 18 + TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Query (for API calls)
- **Build Tool**: Vite
- **Testing**: Jest + React Testing Library

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Validation**: Pydantic
- **Scientific Computing**: NumPy, SciPy
- **API Documentation**: OpenAPI/Swagger (auto-generated)

### Database
- **Primary**: PostgreSQL 15+ with JSONB support
- **Cache**: Redis 7+ for session state
- **Connection Pooling**: SQLAlchemy pool

### Infrastructure
- **Local Development**: Docker Compose
- **Deployment**: Railway/Render/Fly.io (TBD)
- **Environment**: Python virtual environment

### Tools
- **Version Control**: Git
- **Package Management**: pip (Python), npm (Node.js)
- **Code Quality**: Black (Python), ESLint (TypeScript)
- **Testing**: pytest (Python), Jest (JavaScript)

---

## Architecture Patterns

### 1. Layered Architecture
- **Presentation Layer**: React components (UI)
- **Application Layer**: FastAPI routes (API endpoints)
- **Domain Layer**: Business logic (matching engine, Bayesian updates)
- **Data Layer**: SQLAlchemy models, Redis cache

### 2. Repository Pattern
- Database access abstracted through SQLAlchemy models
- Session state managed via Redis cache layer
- Clear separation between data access and business logic

### 3. Service Layer Pattern
- Business logic separated into service modules:
  - `matching_engine.py`: Cosine similarity, ranking
  - `question_selector.py`: Adaptive question selection (Sprint 03+)
  - `bayesian.py`: Parameter updates, uncertainty calculation
  - `session_manager.py`: Session lifecycle management

### 4. Dependency Injection
- FastAPI dependency injection for database sessions, Redis clients
- Enables testing with mock dependencies

---

## System Components

### Frontend (`frontend/`)

#### QuestionDisplay Component
**Purpose**: Displays one question at a time with neutral, conversational UI  
**Technology**: React + TypeScript + Tailwind CSS  
**Interfaces**: Props: `question: Question`, `onSubmit: (response) => void`  
**Dependencies**: React Query for API calls

#### ResultsPage Component
**Purpose**: Shows top 3 match recommendations with explanations  
**Technology**: React + TypeScript + Tailwind CSS  
**Interfaces**: Props: `sessionId: string`  
**Dependencies**: `/result` API endpoint

#### SessionManager Hook
**Purpose**: Manages session state and question flow  
**Technology**: React Query + Custom hooks  
**Interfaces**: `useSession()`, `useQuestion()`, `useResult()`  
**Dependencies**: Backend API endpoints

---

### Backend (`backend/`)

#### API Routes (`backend/api/`)
**Purpose**: Handle HTTP requests and responses  
**Technology**: FastAPI  
**Interfaces**: REST endpoints (see API_SPEC.md)  
**Dependencies**: Domain services, database models

**Routes**:
- `session.py`: `/session/start`, `/session/{id}/result`
- `response.py`: `/response`
- `admin.py`: `/admin/questions`, `/admin/archetypes` (Sprint 07+)

#### Domain Services (`backend/core/`)
**Purpose**: Business logic for matching, Bayesian updates, question selection  
**Technology**: Python + NumPy + SciPy  
**Interfaces**: Functions called by API routes  
**Dependencies**: Models, Redis cache

**Services**:
- `matching_engine.py`: Cosine similarity, ranking
- `question_selector.py`: Adaptive selection (Sprint 03+)
- `bayesian.py`: Parameter updates, uncertainty
- `session_manager.py`: Session lifecycle

#### Data Models (`backend/models/`)
**Purpose**: SQLAlchemy ORM models for database entities  
**Technology**: SQLAlchemy  
**Interfaces**: Database queries via ORM  
**Dependencies**: PostgreSQL database

**Models**:
- `User`: User accounts
- `Session`: Interview sessions
- `Question`: Question bank
- `Response`: User answers
- `Archetype`: Match targets
- `MatchReport`: Recommendation results

#### Utilities (`backend/utils/`)
**Purpose**: Helper functions for vector math, normalization  
**Technology**: NumPy  
**Interfaces**: Pure functions  
**Dependencies**: None

**Utilities**:
- `vector_math.py`: Cosine similarity, vector operations
- `normalization.py`: Likert scale normalization
- `validation.py`: Parameter validation

---

### Data Layer

#### PostgreSQL Database
**Purpose**: Persistent storage for all entities  
**Technology**: PostgreSQL 15+  
**Interfaces**: SQL queries via SQLAlchemy  
**Dependencies**: None

**Schema**:
- JSONB fields for flexible vector storage (10-dimensional arrays)
- Indexes on foreign keys for performance
- Relationships: Session → User, Response → Session, MatchReport → Session

#### Redis Cache
**Purpose**: Fast session state lookups  
**Technology**: Redis 7+  
**Interfaces**: Python redis client  
**Dependencies**: None

**Usage**:
- Cache session state (state_vector, covariance, answered_qids)
- TTL: 24 hours (configurable)
- Key format: `session:{session_id}`

---

## Data Flow

### User Journey Flow
```
User → React UI
  ↓
POST /session/start → FastAPI
  ↓
Create Session (PostgreSQL) → Cache Session (Redis)
  ↓
Return Question → React UI
  ↓
User Answers → POST /response → FastAPI
  ↓
Update Session (PostgreSQL + Redis)
  ↓
Return Next Question → React UI
  ↓
[... repeat until done ...]
  ↓
GET /result → FastAPI
  ↓
Compute Matches (matching_engine.py)
  ↓
Return Recommendations → React UI
  ↓
Display Results Page
```

### Adaptive Engine Flow (Sprint 03+)
```
Current Session State
  ↓
Compute Uncertainty (bayesian.py)
  ↓
Identify High-Uncertainty Parameters
  ↓
Retrieve Candidate Questions (question_selector.py)
  ↓
Compute Information Gain (question_selector.py)
  ↓
Select Best Question (highest gain)
  ↓
Return Question → User
  ↓
User Answers → Bayesian Update (bayesian.py)
  ↓
Update Uncertainty → Repeat
```

---

## Architecture Decisions

### ADR-001: Python Backend for Bayesian Inference
**Date**: 2025-01-27  
**Status**: Accepted

**Context**: ORBIT requires Bayesian parameter updates, entropy calculations, and statistical computing. Need to choose between Python and JavaScript backend.

**Decision**: Use Python (FastAPI) backend with NumPy/SciPy for scientific computing.

**Rationale**:
- Python's scientific ecosystem (NumPy, SciPy) makes Bayesian inference straightforward
- NumPy provides optimized vector operations for 10-dimensional parameter space
- OpenAI API integration is seamless in Python
- Statistical libraries (scipy.stats) support Bayesian updates

**Alternatives Considered**:
1. **JavaScript/Node.js**: Simpler language context, but weaker ML ecosystem
2. **Go**: Fast, but limited scientific computing libraries
3. **Rust**: High performance, but ecosystem maturity concerns

**Consequences**: 
- Positive: Clean, maintainable statistical code; easy OpenAI integration
- Negative: Context switching between Python and TypeScript; two deployment pipelines

---

### ADR-002: JSONB for Vector Storage
**Date**: 2025-01-27  
**Status**: Accepted

**Context**: Need to store 10-dimensional parameter vectors for users and archetypes. Options: 10 separate columns vs JSONB array vs vector extension.

**Decision**: Use PostgreSQL JSONB fields for flexible vector storage.

**Rationale**:
- Flexible: Easy to adjust parameter count without schema changes
- Native JSON operations: PostgreSQL JSONB operators for queries
- Simpler than pgvector extension for MVP
- Sufficient performance for < 100 archetypes

**Alternatives Considered**:
1. **10 separate columns**: Type-safe but rigid, schema changes required for parameter adjustments
2. **pgvector extension**: Optimized for similarity search, but adds complexity

**Consequences**:
- Positive: Flexible schema, easy to extend
- Negative: Slightly slower than normalized columns, but acceptable for scale

---

### ADR-003: Static Flow First, Adaptation Later
**Date**: 2025-01-27  
**Status**: Accepted

**Context**: Sprint 01 goal is end-to-end MVP. Question flow can be static (sequential) or adaptive (Bayesian-driven).

**Decision**: Implement static sequential flow first (Sprint 01), add adaptation incrementally (Sprint 03+).

**Rationale**:
- Reduces Sprint 01 complexity and risk
- Validates core matching logic before investing in adaptive complexity
- Allows incremental testing of Bayesian components
- Aligns with user choice (option 3c)

**Alternatives Considered**:
1. **Adaptive from start**: Higher risk, more complex, harder to debug
2. **Hybrid approach**: Too complex for MVP

**Consequences**:
- Positive: MVP delivered faster, lower risk
- Negative: Refactoring needed in Sprint 03 (technical debt TD-001)

---

### ADR-004: React Query for State Management
**Date**: 2025-01-27  
**Status**: Accepted

**Context**: Need to manage API calls, session state, and question flow in React frontend.

**Decision**: Use React Query for API state management, minimal local state.

**Rationale**:
- React Query handles caching, loading states, error handling automatically
- Reduces boilerplate compared to Redux
- Perfect for REST API integration
- Simple state management sufficient for MVP

**Consequences**:
- Positive: Less code, better UX (caching, loading states)
- Negative: May need additional state management for complex UI later

---

## Security Considerations

### Authentication & Authorization
- **Admin routes**: JWT-based authentication (Sprint 07+)
- **User sessions**: Anonymous sessions (no auth required for MVP)
- **API keys**: OpenAI API key stored in environment variables

### Data Privacy
- **No PII collected**: Only optional email after results (GDPR-compliant)
- **Anonymized responses**: Responses stored separately from emails
- **Session deletion**: DELETE /session/:id removes all related data

### Input Validation
- **Pydantic models**: Validate all API inputs
- **SQL injection**: Prevented via SQLAlchemy ORM
- **XSS**: React escapes HTML by default

### HTTPS
- **Production**: Enforce HTTPS (TLS 1.3)
- **Local development**: HTTP acceptable for MVP

---

## Performance Considerations

### API Response Time
- **Target**: < 200ms for question selection
- **Optimization**: Redis caching for session lookups (< 10ms)
- **Database queries**: Indexed foreign keys, connection pooling

### Matching Performance
- **Target**: < 100ms for cosine similarity with 50 archetypes
- **Optimization**: NumPy vectorized operations
- **Caching**: Consider caching similarity scores if needed (Sprint 07+)

### Frontend Performance
- **Bundle size**: Code splitting with Vite
- **API calls**: React Query caching reduces redundant requests
- **Rendering**: Minimal re-renders with React Query

### Scalability
- **Database**: PostgreSQL scales horizontally with read replicas (future)
- **Redis**: Can scale with Redis Cluster (future)
- **API**: Stateless FastAPI can scale horizontally behind load balancer

---

## Scalability Strategy

### Current (MVP)
- Single PostgreSQL instance
- Single Redis instance
- Single FastAPI server

### Phase 2 (Production)
- PostgreSQL with read replicas
- Redis Cluster for high availability
- Multiple FastAPI instances behind load balancer
- CDN for static assets

### Phase 3 (Scale)
- Database sharding by user region (if needed)
- Redis Cluster with persistence
- Auto-scaling API instances
- Edge caching for question assets

---

## Monitoring & Observability

### Logging
- **Backend**: Structured logging with Python `logging` module
- **Frontend**: Console logging for development, error tracking service (future)
- **Format**: JSON logs for parsing

### Metrics
- **Application**: Session count, question count, completion rate (Sprint 11+)
- **Infrastructure**: CPU, memory, database connection pool
- **API**: Response times, error rates

### Alerting
- **Phase 2**: Set up alerts for error rates > 1%, response times > 500ms
- **Tools**: Sentry for error tracking, Datadog/New Relic for APM (future)

### Tracing
- **Phase 2**: Distributed tracing for request flow (OpenTelemetry)
- **Purpose**: Debug performance bottlenecks in adaptive engine

---

## Technical Debt

| ID | Description | Impact | Effort | Priority | Sprint |
|----|-------------|--------|--------|----------|--------|
| TD-001 | Refactor static flow to adaptive flow | Medium | Medium | Medium | Sprint 03 |
| TD-002 | Add free-text processing architecture | Low | Small | Low | Sprint 19+ |
| TD-003 | Optimize matching for 50+ archetypes | Low | Small | Low | Sprint 07+ |
| TD-004 | Add admin authentication (deferred) | Medium | Medium | Medium | Sprint 07 |

---

## Future Considerations

### Machine Learning Enhancements
- **Custom embedding model**: Train domain-specific embeddings for hobbies
- **Reinforcement learning**: Optimize question selection based on user feedback
- **A/B testing**: Test different question selection strategies

### Integration Opportunities
- **Event APIs**: Eventbrite, Meetup integration for real opportunities
- **Social features**: Share matches with friends, group recommendations
- **Mobile apps**: Native iOS/Android apps (React Native)

### Advanced Features
- **Multi-language support**: Internationalization for questions and archetypes
- **Personalization**: User profiles, match history, preferences
- **Recommendation refinement**: Learn from user feedback on matches

---

*Last Updated: 2025-01-27*
