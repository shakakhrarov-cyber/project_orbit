# Sprint 01 - Plan

## Sprint Goal
Deliver end-to-end MVP with static questionnaire flow and basic matching engine. Users can complete a 20-question interview and receive 3 personalized hobby/role recommendations.

## Sprint Details
- **Sprint Number**: 01
- **Start Date**: 2025-01-27
- **End Date**: 2025-02-03
- **Duration**: 1 week (5 working days)
- **Team Capacity**: 18-21 story points (solo developer with AI agents)

---

## Sprint Backlog

### User Stories Committed

#### US-001: Database Schema Setup
**Priority**: High  
**Story Points**: 5  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-001: Create SQLAlchemy models (User, Session, Question, Response, Archetype, MatchReport) - Estimated: 4 hours
- [ ] TASK-002: Create Alembic migration files - Estimated: 2 hours
- [ ] TASK-003: Define relationships and indexes - Estimated: 2 hours
- [ ] TASK-004: Write unit tests for models - Estimated: 2 hours

**Acceptance Criteria**:
- [ ] Given migrations run, then all tables created successfully
- [ ] Given Session model, then it stores state_vector (JSONB), covariance (JSONB), answered_qids (array)
- [ ] Given Question model, then it stores text, targets, info_weight, type, locale
- [ ] Given Archetype model, then it stores vector (JSONB array), min_requirements, contraindications, resources

---

#### US-002: FastAPI Project Structure
**Priority**: High  
**Story Points**: 3  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-005: Create FastAPI app with CORS and error handling - Estimated: 2 hours
- [ ] TASK-006: Organize routes into modules (session, response, result, admin) - Estimated: 2 hours
- [ ] TASK-007: Configure dependency injection (database, Redis) - Estimated: 2 hours
- [ ] TASK-008: Test Swagger docs at /docs - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given FastAPI app, when started, then Swagger docs available at /docs
- [ ] Given routes, when organized, then they're separated into modules
- [ ] Given dependencies, when injected, then database session available

---

#### US-004: Docker Compose Setup
**Priority**: High  
**Story Points**: 2  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-009: Create docker-compose.yml (postgres, redis, backend) - Estimated: 2 hours
- [ ] TASK-010: Create .env file template - Estimated: 1 hour
- [ ] TASK-011: Test container startup and health checks - Estimated: 1 hour
- [ ] TASK-012: Document setup instructions in README - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given docker-compose up, then all containers start successfully
- [ ] Given containers, when accessed, then PostgreSQL on 5432, Redis on 6379, API on 8000
- [ ] Given migrations, when containers start, then migrations run automatically

---

#### US-009: Seed 20 Questions from JSON
**Priority**: High  
**Story Points**: 2  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-013: Create questions.json with 20 placeholder questions - Estimated: 2 hours
- [ ] TASK-014: Write seed script (seed_questions.py) - Estimated: 2 hours
- [ ] TASK-015: Test idempotent seed (can run multiple times) - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given seed script, when run, then 20 questions imported to database
- [ ] Given questions, when queried, then they cover broad aspects (social, creative, physical)
- [ ] Given seed script, when run again, then no duplicates created

---

#### US-005: Question Display UI Component
**Priority**: High  
**Story Points**: 5  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-016: Create React project with TypeScript and Tailwind CSS - Estimated: 2 hours
- [ ] TASK-017: Build QuestionDisplay.tsx component - Estimated: 4 hours
- [ ] TASK-018: Style with minimalist design (white space, sans-serif) - Estimated: 2 hours
- [ ] TASK-019: Test component rendering - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given question object, when displayed, then question text shows prominently
- [ ] Given interface, when viewed, then no progress indicators visible
- [ ] Given design, when rendered, then follows minimalist principles

---

#### US-010: Static Sequential Question Flow
**Priority**: High  
**Story Points**: 3  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-020: Implement /session/start endpoint (returns first question) - Estimated: 2 hours
- [ ] TASK-021: Implement /response endpoint (accepts answer, returns next question) - Estimated: 3 hours
- [ ] TASK-022: Add session tracking (answered_qids array) - Estimated: 2 hours
- [ ] TASK-023: Test sequential flow (1 → 2 → 3...) - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given session start, when begun, then first question returned
- [ ] Given response submitted, then next question returned
- [ ] Given last question answered, then session completes

---

#### US-013: Seed 5 Archetypes with 10-Dim Vectors
**Priority**: High  
**Story Points**: 2  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-024: Create archetypes.json with 5 archetypes - Estimated: 2 hours
- [ ] TASK-025: Write seed script (seed_archetypes.py) - Estimated: 2 hours
- [ ] TASK-026: Validate vectors are 0-1 range - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given seed script, when run, then 5 archetypes imported
- [ ] Given each archetype, then it has name, vector (10-dim), resources
- [ ] Given vectors, then all values are 0-1 range

---

#### US-014: Cosine Similarity Matching Algorithm
**Priority**: High  
**Story Points**: 3  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-027: Implement cosine_similarity function (NumPy) - Estimated: 2 hours
- [ ] TASK-028: Write unit tests for similarity calculation - Estimated: 2 hours
- [ ] TASK-029: Implement ranking algorithm (sort by similarity) - Estimated: 2 hours
- [ ] TASK-030: Test performance (< 50ms for 50 archetypes) - Estimated: 1 hour

**Acceptance Criteria**:
- [ ] Given user vector and archetype vector, then cosine similarity calculated correctly
- [ ] Given multiple archetypes, then ranked by similarity (highest first)
- [ ] Given unit tests, then math validated

---

#### US-015: Results Page with Recommendations
**Priority**: High  
**Story Points**: 5  
**Owner**: Developer  
**Status**: To Do

**Tasks**:
- [ ] TASK-031: Implement /result endpoint (GET /session/{id}/result) - Estimated: 2 hours
- [ ] TASK-032: Create ResultsPage.tsx component - Estimated: 4 hours
- [ ] TASK-033: Display top 3 matches with fit scores - Estimated: 2 hours
- [ ] TASK-034: Generate simple explanations - Estimated: 2 hours
- [ ] TASK-035: Test end-to-end flow (start → answer → results) - Estimated: 2 hours

**Acceptance Criteria**:
- [ ] Given session completion, then top 3 matches returned
- [ ] Given each match, then shows rank, name, fit score (0-1), explanation
- [ ] Given results page, then displays correctly

---

## Sprint Metrics

### Commitment
- **Total Story Points**: 30 points (committed: 18-21 achievable)
- **Number of Stories**: 9
- **Number of Tasks**: 35

### Team Velocity (Historical)
- Sprint -2: N/A (new project)
- Sprint -1: N/A (new project)
- **Projected for Sprint 01**: 18-21 points (realistic for 1 week solo dev)

### Sprint Goal Achievement Criteria
- [ ] End-to-end user flow working (start → answer → results)
- [ ] Database schema and API foundation complete
- [ ] Front-end displays questions and results
- [ ] Basic matching algorithm functional
- [ ] Static flow works (no adaptation yet)

---

## Day-by-Day Breakdown

### Day 1 (Monday) - Foundation
**Focus**: Database schema, FastAPI setup, Docker

**Tasks**:
- TASK-001: SQLAlchemy models (4h)
- TASK-002: Alembic migrations (2h)
- TASK-005: FastAPI app structure (2h)

**Deliverables**: Database schema ready, FastAPI app running

---

### Day 2 (Tuesday) - Infrastructure & Seed Data
**Focus**: Docker, seed scripts, API endpoints

**Tasks**:
- TASK-009: Docker Compose setup (2h)
- TASK-013: Questions JSON + seed script (2h)
- TASK-024: Archetypes JSON + seed script (2h)
- TASK-020: /session/start endpoint (2h)

**Deliverables**: Docker running, seed data loaded, session start endpoint working

---

### Day 3 (Wednesday) - Front-End Setup
**Focus**: React app, question display, response collection

**Tasks**:
- TASK-016: React project setup (2h)
- TASK-017: QuestionDisplay component (4h)
- TASK-018: Styling (2h)

**Deliverables**: Front-end displays questions

---

### Day 4 (Thursday) - Integration & Flow
**Focus**: API integration, static flow, matching

**Tasks**:
- TASK-021: /response endpoint (3h)
- TASK-027: Cosine similarity function (2h)
- TASK-028: Matching unit tests (2h)
- TASK-031: /result endpoint (2h)

**Deliverables**: Static flow working, matching algorithm functional

---

### Day 5 (Friday) - Results & Testing
**Focus**: Results page, end-to-end testing, polish

**Tasks**:
- TASK-032: ResultsPage component (4h)
- TASK-034: Explanation generation (2h)
- TASK-035: End-to-end testing (2h)
- Polish and bug fixes (2h)

**Deliverables**: End-to-end MVP complete

---

## Definition of Done
A story is considered "Done" when:
- [ ] Code is written and follows coding standards
- [ ] Code is reviewed (self-review for solo dev)
- [ ] Unit tests are written and passing (where applicable)
- [ ] Integration tests passing (for API endpoints)
- [ ] Documentation updated (README, API docs)
- [ ] Acceptance criteria are met
- [ ] Feature works end-to-end

---

## Risks & Dependencies

### Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Docker setup complexity** | Medium | High | Use simple docker-compose.yml, document thoroughly |
| **Time pressure (1 week)** | High | High | Focus on MVP only, defer polish to Sprint 02 |
| **React state management** | Low | Medium | Use React Query for API calls, keep state simple |
| **Cosine similarity math** | Low | Medium | Use NumPy, write unit tests for validation |

### Dependencies
- **External**: OpenAI API key not needed for Sprint 01 (deferred to Sprint 19+)
- **External**: PostgreSQL and Redis must be available (via Docker)
- **Internal**: US-001 must complete before US-002, US-009, US-013
- **Internal**: US-005 must complete before US-010, US-015

---

## Sprint Planning Notes

**Date**: 2025-01-27  
**Attendees**: Developer (solo)

**Discussion Points**:
- Sprint 01 focuses on end-to-end MVP with static flow (per user choice 3c)
- Adaptive engine deferred to Sprint 03+ to reduce risk
- Realistic capacity: 18-21 points achievable in 1 week solo dev
- Results page explanations will be simple (reference matched parameters)

**Decisions Made**:
- **Decision 1**: Start with static flow, add adaptation incrementally (reduces complexity)
- **Decision 2**: Use placeholder explanations for matches (simple parameter references)
- **Decision 3**: Defer responsive design polish to Sprint 02 if time runs short
- **Decision 4**: Focus on desktop-first, mobile polish later

**Action Items**:
- [ ] Set up development environment (Day 1)
- [ ] Create seed data files (Day 2)
- [ ] Test end-to-end flow before Sprint end (Day 5)

---

## Success Criteria

Sprint 01 is successful if:
- ✅ User can start session and see first question
- ✅ User can answer 20 questions sequentially
- ✅ User receives top 3 match recommendations
- ✅ Results display with fit scores and explanations
- ✅ Database stores all entities correctly
- ✅ API endpoints functional and tested

**Stretch Goals** (if time permits):
- Responsive design (mobile support)
- Session termination logic (40 question limit)
- Better explanation generation

---

*Created: 2025-01-27*  
*Last Updated: 2025-01-27*
