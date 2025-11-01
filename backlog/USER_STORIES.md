# User Stories - ORBIT Project

## Story Template
Each user story follows the format:
- **As a** [type of user]
- **I want** [some goal]
- **So that** [some reason/benefit]

---

## Epic: EPIC-001 - Core Infrastructure & Data Model

### US-001: Database Schema Setup
**Epic**: EPIC-001  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** developer  
**I want** PostgreSQL database with complete schema for all ORBIT entities  
**So that** the system can store users, sessions, questions, responses, archetypes, and match reports

**Acceptance Criteria**:
- [ ] Given a fresh database, when I run migrations, then tables are created for User, Session, Question, Response, Archetype, MatchReport
- [ ] Given a Session entity, when I store it, then it includes user_id, state_vector (JSONB), covariance (JSONB), answered_qids (array)
- [ ] Given a Question entity, when I store it, then it includes text, targets (array), info_weight (array), difficulty, type, locale
- [ ] Given an Archetype entity, when I store it, then it includes name, vector (JSONB array), min_requirements (JSONB), contraindications (JSONB), resources (JSONB)
- [ ] Given any entity, when I query it, then relationships are properly indexed

**Technical Notes**:
- Use SQLAlchemy ORM with Alembic migrations
- JSONB fields for flexible vector storage (10-dimensional arrays)
- Foreign key relationships: Session → User, Response → Session, MatchReport → Session
- Indexes on session_id, user_id, question_id for performance

**Definition of Done**:
- [ ] Schema defined in SQLAlchemy models
- [ ] Migration files created and tested
- [ ] Unit tests for model relationships
- [ ] Documentation updated with ER diagram

**Dependencies**: None

---

### US-002: FastAPI Project Structure
**Epic**: EPIC-001  
**Priority**: High  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** developer  
**I want** FastAPI project with proper structure and dependency injection  
**So that** I can build endpoints efficiently and maintain clean code

**Acceptance Criteria**:
- [ ] Given a new project, when I start it, then FastAPI app is configured with CORS, error handling, and logging
- [ ] Given API routes, when I organize them, then they're separated into modules (session, response, result, admin)
- [ ] Given dependencies, when I inject them, then database session and Redis client are available to routes
- [ ] Given the API, when I access it, then OpenAPI/Swagger docs are available at /docs

**Technical Notes**:
- Structure: `backend/api/` (routes), `backend/core/` (business logic), `backend/models/` (SQLAlchemy), `backend/utils/` (helpers)
- Use Pydantic for request/response validation
- Environment variables for config (database URL, Redis URL, OpenAI key)

**Definition of Done**:
- [ ] Project structure created
- [ ] Basic health check endpoint working
- [ ] Dependency injection configured
- [ ] Swagger docs accessible

**Dependencies**: US-001

---

### US-003: Redis Session Caching
**Epic**: EPIC-001  
**Priority**: Medium  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** Redis cache for session state management  
**So that** session lookups are fast and reduce database load

**Acceptance Criteria**:
- [ ] Given a new session, when created, then session state is cached in Redis with TTL
- [ ] Given a cached session, when retrieved, then response time < 10ms
- [ ] Given session updates, when saved, then both Redis and database are updated
- [ ] Given Redis failure, when accessed, then system falls back to database

**Technical Notes**:
- Redis key format: `session:{session_id}`
- TTL: 24 hours (configurable)
- Cache session state_vector, covariance, answered_qids

**Definition of Done**:
- [ ] Redis client configured
- [ ] Cache layer implemented
- [ ] Fallback logic tested
- [ ] Performance tests show < 10ms cache hits

**Dependencies**: US-002

---

### US-004: Docker Compose Setup
**Epic**: EPIC-001  
**Priority**: High  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** developer  
**I want** Docker Compose configuration for local development  
**So that** I can run PostgreSQL, Redis, and the API locally with one command

**Acceptance Criteria**:
- [ ] Given Docker is installed, when I run `docker-compose up`, then PostgreSQL, Redis, and API containers start
- [ ] Given the containers, when I access them, then PostgreSQL is on port 5432, Redis on 6379, API on 8000
- [ ] Given database migrations, when containers start, then migrations run automatically
- [ ] Given container logs, when I view them, then they're readable and useful

**Technical Notes**:
- `docker-compose.yml` with services: postgres, redis, backend (API)
- Environment variables in `.env` file
- Volume mounts for database persistence
- Health checks for service dependencies

**Definition of Done**:
- [ ] docker-compose.yml created
- [ ] Containers start successfully
- [ ] Documentation updated with setup instructions
- [ ] README includes Docker commands

**Dependencies**: US-001, US-002, US-003

---

## Epic: EPIC-002 - Front-End User Interface

### US-005: Question Display UI Component
**Epic**: EPIC-002  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** user  
**I want** to see one question at a time in a clean, minimalist interface  
**So that** I can focus on answering without distraction

**Acceptance Criteria**:
- [ ] Given a question, when displayed, then it shows question text prominently
- [ ] Given the interface, when I view it, then there's no visible progress indicator or scoring logic
- [ ] Given white space, when designed, then it follows minimalist design principles (sans-serif font, soft colors)
- [ ] Given the question, when displayed, then it's clear and conversational (not evaluative tone)

**Technical Notes**:
- React component: `QuestionDisplay.tsx`
- Use Tailwind CSS for styling
- No progress bars, no "Question X of Y" text
- Props: question object (text, type, options)

**Definition of Done**:
- [ ] Component created and styled
- [ ] Question text renders correctly
- [ ] Design matches PRD UX principles
- [ ] Component is responsive

**Dependencies**: US-002 (API endpoint needed)

---

### US-006: Response Collection (Multiple Types)
**Epic**: EPIC-002  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** user  
**I want** to answer multiple-choice, Likert scale, and slider questions  
**So that** I can provide responses in different formats

**Acceptance Criteria**:
- [ ] Given a multiple-choice question, when displayed, then I can select one option
- [ ] Given a Likert scale question, when displayed, then I can select 1-5 rating
- [ ] Given a slider question, when displayed, then I can drag to select value
- [ ] Given any response, when submitted, then it's sent to API and validated

**Technical Notes**:
- Components: `MultipleChoiceInput.tsx`, `LikertScaleInput.tsx`, `SliderInput.tsx`
- Validation: Ensure response matches question type
- State management: React Query for API calls

**Definition of Done**:
- [ ] All three input types implemented
- [ ] Validation working
- [ ] API integration tested
- [ ] Error handling for invalid responses

**Dependencies**: US-005, US-002

---

### US-007: Results Page with Recommendations
**Epic**: EPIC-002  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** user  
**I want** to see my match results with 2-3 recommendations and clear explanations  
**So that** I understand why these hobbies/roles match my preferences

**Acceptance Criteria**:
- [ ] Given session completion, when I view results, then top 3 matches are displayed
- [ ] Given each match, when displayed, then it shows hobby name, fit score (0-1), and explanation
- [ ] Given the results, when displayed, then explanations are clear and non-technical
- [ ] Given resources, when available, then links to opportunities are provided

**Technical Notes**:
- Component: `ResultsPage.tsx`
- Fetch from `/result` endpoint
- Display: Rank, Name, Fit Score (0.88), Explanation text
- Optional: Confidence metrics (if available)

**Definition of Done**:
- [ ] Results page designed and implemented
- [ ] API integration working
- [ ] Explanations render correctly
- [ ] Links to resources functional

**Dependencies**: US-002, US-014 (matching engine)

---

### US-008: Responsive Design (Mobile + Desktop)
**Epic**: EPIC-002  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 02

**Story**:  
**As a** user  
**I want** the interface to work well on mobile and desktop  
**So that** I can use ORBIT on any device

**Acceptance Criteria**:
- [ ] Given mobile viewport, when displayed, then interface is usable (touch-friendly buttons)
- [ ] Given desktop viewport, when displayed, then layout is optimized for larger screens
- [ ] Given any screen size, when viewed, then text is readable and buttons are accessible
- [ ] Given responsive breakpoints, when resized, then layout adapts smoothly

**Technical Notes**:
- Tailwind CSS responsive utilities (sm:, md:, lg:)
- Mobile-first approach
- Test on Chrome DevTools device emulation

**Definition of Done**:
- [ ] Mobile layout tested and working
- [ ] Desktop layout optimized
- [ ] Responsive breakpoints validated
- [ ] Cross-browser testing done

**Dependencies**: US-005, US-006, US-007

---

### US-025: Accessibility Support (Keyboard Nav, ARIA)
**Epic**: EPIC-002  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 02

**Story**:  
**As a** user with accessibility needs  
**I want** keyboard navigation and ARIA labels  
**So that** I can use ORBIT with assistive technologies

**Acceptance Criteria**:
- [ ] Given keyboard navigation, when I tab through interface, then focus is visible and logical
- [ ] Given screen readers, when used, then ARIA labels provide context
- [ ] Given form inputs, when accessed, then they're properly labeled
- [ ] Given buttons, when activated, then keyboard shortcuts work

**Technical Notes**:
- ARIA labels on all interactive elements
- Focus management for question transitions
- Keyboard shortcuts: Enter to submit, Esc to cancel (if needed)

**Definition of Done**:
- [ ] Keyboard navigation tested
- [ ] ARIA labels added
- [ ] Screen reader tested (VoiceOver/NVDA)
- [ ] WCAG AA compliance verified

**Dependencies**: US-005, US-006

---

## Epic: EPIC-003 - Static Interview Flow (MVP)

### US-009: Seed 20 Questions from JSON
**Epic**: EPIC-003  
**Priority**: High  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** to load 20 questions from seed data  
**So that** I can test the interview flow without a full question bank

**Acceptance Criteria**:
- [ ] Given seed data file, when loaded, then 20 questions are imported to database
- [ ] Given questions, when queried, then they cover broad aspects (social, creative, physical)
- [ ] Given question types, when displayed, then they include multiple-choice, Likert, slider
- [ ] Given seed script, when run, then it's idempotent (can run multiple times safely)

**Technical Notes**:
- File: `backend/seed_data/questions.json`
- Seed script: `backend/scripts/seed_questions.py`
- Questions target different parameters (even distribution)

**Definition of Done**:
- [ ] JSON file created with 20 questions
- [ ] Seed script implemented
- [ ] Questions loaded into database
- [ ] Script is idempotent

**Dependencies**: US-001

---

### US-010: Static Sequential Question Flow
**Epic**: EPIC-003  
**Priority**: High  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** user  
**I want** to progress through questions sequentially (no adaptation yet)  
**So that** I can complete the interview and see results

**Acceptance Criteria**:
- [ ] Given session start, when begun, then first question is displayed
- [ ] Given a response, when submitted, then next question is shown
- [ ] Given question order, when displayed, then it's linear (1, 2, 3...)
- [ ] Given last question, when answered, then session completes

**Technical Notes**:
- API endpoint: `/session/start` → returns first question
- API endpoint: `/response` → accepts answer, returns next question or done flag
- Session tracks `answered_qids` array
- Simple logic: next_question = questions[answered_qids.length]

**Definition of Done**:
- [ ] Start session endpoint working
- [ ] Response submission endpoint working
- [ ] Question flow is sequential
- [ ] Session completion detected

**Dependencies**: US-009, US-005, US-006

---

### US-011: Session State Management
**Epic**: EPIC-003  
**Priority**: High  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** to track session state and answered questions  
**So that** I can resume sessions and compute matches

**Acceptance Criteria**:
- [ ] Given a new session, when created, then session record is stored with user_id
- [ ] Given responses, when saved, then answered_qids array is updated
- [ ] Given session retrieval, when requested, then state is returned correctly
- [ ] Given session updates, when saved, then Redis cache is updated

**Technical Notes**:
- Session model: id, user_id, state_vector (null initially), covariance (null), answered_qids ([]), created_at, updated_at
- Cache session in Redis for fast lookups
- Update both DB and cache on response

**Definition of Done**:
- [ ] Session creation working
- [ ] Response tracking working
- [ ] State persistence verified
- [ ] Cache sync working

**Dependencies**: US-001, US-003, US-010

---

### US-012: Session Termination Logic
**Epic**: EPIC-003  
**Priority**: Medium  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** to terminate session after 40 questions or 20 minutes  
**So that** sessions don't run indefinitely

**Acceptance Criteria**:
- [ ] Given 40 questions answered, when 40th response submitted, then session terminates
- [ ] Given 20 minutes elapsed, when checked, then session terminates
- [ ] Given termination, when triggered, then done flag is returned
- [ ] Given termination, when done, then results can be generated

**Technical Notes**:
- Check question count: `len(answered_qids) >= 40`
- Check time: `session.created_at + timedelta(minutes=20) < now()`
- Return `{"done": true}` instead of next question

**Definition of Done**:
- [ ] Question limit enforced
- [ ] Time limit enforced
- [ ] Termination logic tested
- [ ] Edge cases handled

**Dependencies**: US-010, US-011

---

## Epic: EPIC-004 - Basic Matching Engine (MVP)

### US-013: Seed 5 Archetypes with 10-Dim Vectors
**Epic**: EPIC-004  
**Priority**: High  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** to load 5 archetypes with 10-dimensional vectors  
**So that** I can test the matching engine

**Acceptance Criteria**:
- [ ] Given seed data file, when loaded, then 5 archetypes are imported
- [ ] Given each archetype, when stored, then it has name, vector (10-dim), min_requirements, contraindications, resources
- [ ] Given vectors, when checked, then all values are 0-1 range
- [ ] Given seed script, when run, then it's idempotent

**Technical Notes**:
- File: `backend/seed_data/archetypes.json`
- Example archetypes: Pottery Class, Trail Running Group, Photography Walks, Book Club, Coding Workshop
- Vectors represent ideal parameter means

**Definition of Done**:
- [ ] JSON file created with 5 archetypes
- [ ] Seed script implemented
- [ ] Archetypes loaded into database
- [ ] Validation ensures 0-1 range

**Dependencies**: US-001

---

### US-014: Cosine Similarity Matching Algorithm
**Epic**: EPIC-004  
**Priority**: High  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** system  
**I want** to compute cosine similarity between user vector and archetypes  
**So that** I can rank matches accurately

**Acceptance Criteria**:
- [ ] Given user vector and archetype vector, when computed, then cosine similarity is calculated correctly
- [ ] Given multiple archetypes, when ranked, then they're sorted by similarity (highest first)
- [ ] Given similarity calculation, when executed, then it handles 10-dimensional vectors
- [ ] Given unit tests, when run, then cosine similarity math is validated

**Technical Notes**:
- Use NumPy for vector operations: `np.dot(u, a) / (np.linalg.norm(u) * np.linalg.norm(a))`
- Function: `compute_cosine_similarity(user_vector, archetype_vector) → float`
- Handle edge cases: zero vectors, normalization

**Definition of Done**:
- [ ] Cosine similarity function implemented
- [ ] Unit tests passing (math validation)
- [ ] Ranking algorithm working
- [ ] Performance: < 50ms for 50 archetypes

**Dependencies**: US-013

---

### US-015: Results Page with Recommendations
**Epic**: EPIC-004  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 01

**Story**:  
**As a** user  
**I want** to see top 3 matches with fit scores and explanations  
**So that** I understand my recommendations

**Acceptance Criteria**:
- [ ] Given session completion, when results requested, then top 3 archetypes are returned
- [ ] Given each match, when displayed, then it shows rank, name, fit score (0-1), explanation
- [ ] Given explanations, when generated, then they reference matched parameters
- [ ] Given resources, when available, then links are provided

**Technical Notes**:
- API endpoint: `/result` → GET /session/{session_id}/result
- Generate explanations: "Matches creative drive (0.8), low social need (0.2), tactile learning (0.9)"
- Format: `[{"rank": 1, "name": "Pottery Class", "fit": 0.88, "explanation": "..."}, ...]`

**Definition of Done**:
- [ ] Results endpoint implemented
- [ ] Top 3 matches returned
- [ ] Explanations generated
- [ ] Front-end displays results correctly

**Dependencies**: US-014, US-007

---

### US-016: Match Explanation Generation
**Epic**: EPIC-004  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 02

**Story**:  
**As a** user  
**I want** clear explanations for why matches were recommended  
**So that** I understand the reasoning behind suggestions

**Acceptance Criteria**:
- [ ] Given a match, when explanation generated, then it references top 3 matched parameters
- [ ] Given explanations, when displayed, then they're non-technical and conversational
- [ ] Given parameter names, when referenced, then they use user-friendly terms (e.g., "social preference" not "param_0")
- [ ] Given low fit scores, when explained, then uncertainty is acknowledged

**Technical Notes**:
- Parameter mapping: `{0: "social preference", 1: "physical intensity", ...}`
- Explanation template: "Matches [param1] ([value]), [param2] ([value]), [param3] ([value])"
- Example: "Matches creative drive (0.8), low social need (0.2), tactile learning (0.9)"

**Definition of Done**:
- [ ] Explanation generation logic implemented
- [ ] Template system working
- [ ] User-friendly parameter names used
- [ ] Explanations tested for clarity

**Dependencies**: US-014, US-015

---

## Epic: EPIC-005 - Adaptive Engine (Bayesian Inference)

### US-017: Initialize User Parameter Vector
**Epic**: EPIC-005  
**Priority**: High  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 03

**Story**:  
**As a** system  
**I want** to initialize user parameter vector with 0.5 ± 0.25 variance  
**So that** I have a starting point for Bayesian updates

**Acceptance Criteria**:
- [ ] Given new session, when created, then parameter vector initialized to [0.5, 0.5, ..., 0.5] (10 dims)
- [ ] Given variance, when initialized, then covariance matrix has 0.25² diagonal values
- [ ] Given initialization, when stored, then state_vector and covariance saved to session
- [ ] Given unit tests, when run, then initialization math is validated

**Technical Notes**:
- Function: `initialize_parameter_vector() → (mean_vector, covariance_matrix)`
- Mean: `np.array([0.5] * 10)`
- Covariance: `np.eye(10) * 0.25²` (diagonal matrix)

**Definition of Done**:
- [ ] Initialization function implemented
- [ ] Unit tests passing
- [ ] Session stores vector and covariance
- [ ] Documentation updated

**Dependencies**: US-011

---

### US-018: Bayesian Parameter Update Logic
**Epic**: EPIC-005  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 03

**Story**:  
**As a** system  
**I want** to update parameter vector using Bayesian inference  
**So that** I can learn about users from their responses

**Acceptance Criteria**:
- [ ] Given prior mean and covariance, when response received, then posterior mean and covariance computed
- [ ] Given Likert answer, when processed, then it's normalized to 0-1 and updates corresponding parameters
- [ ] Given parameter targets, when question answered, then only targeted parameters are updated
- [ ] Given unit tests, when run, then Bayesian update math is validated

**Technical Notes**:
- Function: `bayesian_update(prior_mean, prior_cov, observation, likelihood_cov) → (posterior_mean, posterior_cov)`
- Use NumPy/SciPy for matrix operations
- Likert normalization: `(answer - 1) / (scale_max - 1)` → maps to 0-1

**Definition of Done**:
- [ ] Bayesian update function implemented
- [ ] Parameter targeting working
- [ ] Unit tests passing (math validation)
- [ ] Documentation includes mathematical references

**Dependencies**: US-017

---

### US-019: Uncertainty Calculation (Covariance Tracking)
**Epic**: EPIC-005  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 03

**Story**:  
**As a** system  
**I want** to track uncertainty for each parameter via covariance matrix  
**So that** I can identify which parameters need more information

**Acceptance Criteria**:
- [ ] Given covariance matrix, when uncertainty computed, then diagonal values represent parameter variance
- [ ] Given average uncertainty, when calculated, then it's mean of diagonal variances
- [ ] Given uncertainty threshold, when checked, then I can determine if session should terminate (< 0.12)
- [ ] Given unit tests, when run, then uncertainty calculation is validated

**Technical Notes**:
- Function: `compute_uncertainty(covariance_matrix) → float`
- Average uncertainty: `np.mean(np.diag(covariance_matrix))`
- Threshold: 0.12 (from PRD Section 5.2)

**Definition of Done**:
- [ ] Uncertainty calculation implemented
- [ ] Average uncertainty computed correctly
- [ ] Unit tests passing
- [ ] Threshold logic working

**Dependencies**: US-018

---

### US-020: Information Gain Calculation
**Epic**: EPIC-005  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 04

**Story**:  
**As a** system  
**I want** to calculate expected information gain for candidate questions  
**So that** I can select the most informative question next

**Acceptance Criteria**:
- [ ] Given current covariance and question, when information gain computed, then entropy reduction is calculated
- [ ] Given information gain, when ranked, then higher gain = more informative question
- [ ] Given unit tests, when run, then information gain math is validated
- [ ] Given performance, when computed, then it handles 10 candidate questions efficiently

**Technical Notes**:
- Function: `compute_information_gain(current_cov, question_targets, question_weights) → float`
- Information gain = entropy reduction = expected reduction in parameter uncertainty
- Formula: `gain = sum(weight_i * variance_reduction_i) for i in question_targets`

**Definition of Done**:
- [ ] Information gain function implemented
- [ ] Unit tests passing
- [ ] Performance optimized (< 10ms per question)
- [ ] Documentation includes formula

**Dependencies**: US-019

---

### US-021: Question Selection Algorithm (Entropy-Based)
**Epic**: EPIC-005  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 04-05

**Story**:  
**As a** system  
**I want** to select next question based on highest uncertainty and information gain  
**So that** I efficiently converge to confident parameter estimates

**Acceptance Criteria**:
- [ ] Given current state, when question selected, then algorithm identifies parameters with highest uncertainty
- [ ] Given candidate questions, when evaluated, then top 10 candidates are retrieved
- [ ] Given information gain, when computed, then highest-gain question is selected
- [ ] Given diversity constraint, when applied, then algorithm avoids repetitive questions
- [ ] Given fatigue constraint, when applied, then algorithm considers question difficulty

**Technical Notes**:
- Algorithm (from PRD Section 5.2):
  1. Identify parameters with highest uncertainty
  2. Retrieve 10 candidate questions targeting those parameters
  3. Compute expected information gain for each
  4. Select highest-ranked question (subject to diversity/fatigue)
- Function: `select_next_question(session, question_bank) → Question`

**Definition of Done**:
- [ ] Selection algorithm implemented
- [ ] Information gain integration working
- [ ] Diversity/fatigue constraints applied
- [ ] Unit tests for selection logic
- [ ] Performance: < 100ms for question selection

**Dependencies**: US-020, US-009

---

### US-022: Adaptive Session Termination
**Epic**: EPIC-005  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 04

**Story**:  
**As a** system  
**I want** to terminate session when average uncertainty < 0.12  
**So that** I don't ask unnecessary questions

**Acceptance Criteria**:
- [ ] Given uncertainty check, when computed, then average uncertainty compared to threshold
- [ ] Given threshold met, when detected, then session terminates (done flag)
- [ ] Given termination, when triggered, then final vector and covariance stored
- [ ] Given unit tests, when run, then termination logic is validated

**Technical Notes**:
- Check: `average_uncertainty < 0.12`
- Store final state before terminating
- Return `{"done": true, "final_vector": ..., "covariance": ...}`

**Definition of Done**:
- [ ] Termination logic implemented
- [ ] Threshold check working
- [ ] Final state stored correctly
- [ ] Unit tests passing

**Dependencies**: US-019, US-021

---

### US-023: Likert Answer Normalization
**Epic**: EPIC-005  
**Priority**: Medium  
**Story Points**: 2  
**Status**: To Do  
**Sprint**: Sprint 03

**Story**:  
**As a** system  
**I want** to normalize Likert answers to continuous 0-1 values  
**So that** they can be used in Bayesian updates

**Acceptance Criteria**:
- [ ] Given Likert answer (1-5), when normalized, then it maps to 0-1 range
- [ ] Given different scales, when normalized, then formula works for 1-5, 1-7, etc.
- [ ] Given unit tests, when run, then normalization math is validated
- [ ] Given edge cases, when handled, then min/max values map correctly

**Technical Notes**:
- Formula: `normalized = (answer - min) / (max - min)`
- For 1-5 scale: `normalized = (answer - 1) / 4`
- Function: `normalize_likert(answer, scale_min, scale_max) → float`

**Definition of Done**:
- [ ] Normalization function implemented
- [ ] Unit tests passing
- [ ] Edge cases handled
- [ ] Documentation updated

**Dependencies**: US-018

---

## Epic: EPIC-006 - Admin Tools (Sprint 07+)

### US-026: Admin Authentication System
**Epic**: EPIC-006  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 07

**Story**:  
**As an** admin  
**I want** secure authentication to access admin tools  
**So that** only authorized users can manage questions and archetypes

**Acceptance Criteria**:
- [ ] Given admin login, when accessed, then username/password authentication works
- [ ] Given JWT tokens, when issued, then admin sessions are secure
- [ ] Given protected routes, when accessed, then admin-only endpoints require auth
- [ ] Given logout, when triggered, then session is invalidated

**Technical Notes**:
- FastAPI: `python-jose` for JWT tokens
- Password hashing: `bcrypt`
- Admin routes: `/admin/*` require authentication

**Definition of Done**:
- [ ] Authentication implemented
- [ ] JWT tokens working
- [ ] Protected routes secured
- [ ] Logout functional

**Dependencies**: US-002

---

### US-027: Question CRUD Interface
**Epic**: EPIC-006  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 08

**Story**:  
**As an** admin  
**I want** to create, read, update, and delete questions  
**So that** I can manage the question bank without developer help

**Acceptance Criteria**:
- [ ] Given question creation, when submitted, then question is saved to database
- [ ] Given question list, when viewed, then all questions are displayed with pagination
- [ ] Given question edit, when updated, then changes are saved
- [ ] Given question delete, when deleted, then question is removed (soft delete)

**Technical Notes**:
- API endpoints: POST/PUT/DELETE `/admin/questions`
- Front-end: React admin panel with forms
- Validation: Ensure required fields present

**Definition of Done**:
- [ ] CRUD operations working
- [ ] Admin UI implemented
- [ ] Validation working
- [ ] Pagination functional

**Dependencies**: US-026

---

### US-028: Question Parameter Targeting UI
**Epic**: EPIC-006  
**Priority**: Medium  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 08

**Story**:  
**As an** admin  
**I want** to specify which parameters a question targets and their weights  
**So that** questions are properly connected to the adaptive engine

**Acceptance Criteria**:
- [ ] Given question creation, when editing, then I can select target parameters (checkboxes)
- [ ] Given parameter weights, when specified, then I can set info_weight for each target
- [ ] Given validation, when saved, then targets and weights arrays match length
- [ ] Given UI, when displayed, then parameter names are user-friendly

**Technical Notes**:
- UI component: Multi-select with sliders for weights
- Parameter mapping: Display friendly names (e.g., "Social Preference" not "param_0")
- Validation: `len(targets) == len(info_weights)`

**Definition of Done**:
- [ ] Parameter targeting UI implemented
- [ ] Weight sliders working
- [ ] Validation functional
- [ ] User-friendly parameter names

**Dependencies**: US-027

---

### US-029: Archetype CRUD Interface
**Epic**: EPIC-006  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 09

**Story**:  
**As an** admin  
**I want** to create, read, update, and delete archetypes  
**So that** I can manage the archetype library

**Acceptance Criteria**:
- [ ] Given archetype creation, when submitted, then archetype is saved with vector
- [ ] Given archetype list, when viewed, then all archetypes are displayed
- [ ] Given archetype edit, when updated, then changes are saved
- [ ] Given archetype delete, when deleted, then archetype is removed

**Technical Notes**:
- API endpoints: POST/PUT/DELETE `/admin/archetypes`
- Front-end: React admin panel
- Vector editing: 10 sliders for parameter values (0-1)

**Definition of Done**:
- [ ] CRUD operations working
- [ ] Admin UI implemented
- [ ] Vector editing functional
- [ ] Validation working

**Dependencies**: US-026

---

### US-030: Archetype Vector Editor
**Epic**: EPIC-006  
**Priority**: Medium  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 09

**Story**:  
**As an** admin  
**I want** to edit archetype 10-dimensional vectors visually  
**So that** I can fine-tune matching behavior

**Acceptance Criteria**:
- [ ] Given vector editor, when displayed, then 10 sliders shown (one per parameter)
- [ ] Given parameter names, when displayed, then friendly names are used
- [ ] Given value changes, when updated, then vector is updated in real-time
- [ ] Given validation, when saved, then all values are 0-1 range

**Technical Notes**:
- UI component: 10 sliders with labels
- Real-time preview: Show updated vector
- Validation: Ensure 0 ≤ value ≤ 1

**Definition of Done**:
- [ ] Vector editor implemented
- [ ] Sliders functional
- [ ] Validation working
- [ ] User-friendly parameter names

**Dependencies**: US-029

---

## Epic: EPIC-007 - Analytics & Metrics Dashboard (Sprint 11+)

### US-031: Metrics Collection System
**Epic**: EPIC-007  
**Priority**: High  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 11

**Story**:  
**As a** system  
**I want** to collect metrics on sessions, questions, and matches  
**So that** I can analyze performance

**Acceptance Criteria**:
- [ ] Given session completion, when finished, then metrics are logged
- [ ] Given metrics, when stored, then they include: question count, completion time, match scores
- [ ] Given question performance, when tracked, then question effectiveness is measured
- [ ] Given metrics storage, when queried, then data is available for dashboard

**Technical Notes**:
- Metrics table: session_id, question_count, completion_time, avg_uncertainty, match_scores
- Async logging: Don't block session completion
- Batch processing: Aggregate metrics periodically

**Definition of Done**:
- [ ] Metrics collection implemented
- [ ] Data stored in database
- [ ] Async logging working
- [ ] Query performance optimized

**Dependencies**: US-011

---

### US-032: Dashboard UI with Charts
**Epic**: EPIC-007  
**Priority**: High  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 12

**Story**:  
**As an** admin  
**I want** a dashboard with charts showing key metrics  
**So that** I can monitor system performance

**Acceptance Criteria**:
- [ ] Given dashboard, when viewed, then charts display: average question count, completion rate, match satisfaction
- [ ] Given time range, when selected, then metrics filtered by date
- [ ] Given charts, when displayed, then they're interactive (zoom, filter)
- [ ] Given performance, when loaded, then dashboard loads in < 2 seconds

**Technical Notes**:
- Chart library: Recharts or Chart.js
- Metrics: Average questions, completion rate, satisfaction score
- Time range selector: Last 7 days, 30 days, 90 days

**Definition of Done**:
- [ ] Dashboard UI implemented
- [ ] Charts rendering correctly
- [ ] Time filtering working
- [ ] Performance optimized

**Dependencies**: US-031

---

### US-033: Question Performance Analysis
**Epic**: EPIC-007  
**Priority**: Medium  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 13

**Story**:  
**As an** admin  
**I want** to see which questions are most effective  
**So that** I can optimize the question bank

**Acceptance Criteria**:
- [ ] Given question analysis, when viewed, then each question shows: times asked, avg information gain, dropout rate
- [ ] Given question ranking, when displayed, then questions ranked by effectiveness
- [ ] Given insights, when generated, then recommendations provided (e.g., "remove low-gain questions")

**Technical Notes**:
- Metrics: question_id, times_asked, avg_info_gain, dropout_rate
- Analysis: Identify low-performing questions
- UI: Table with sortable columns

**Definition of Done**:
- [ ] Analysis implemented
- [ ] Question metrics calculated
- [ ] Ranking functional
- [ ] Insights generated

**Dependencies**: US-031, US-021

---

### US-034: User Completion Rate Tracking
**Epic**: EPIC-007  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 11

**Story**:  
**As an** admin  
**I want** to track user completion rates  
**So that** I can monitor engagement

**Acceptance Criteria**:
- [ ] Given session tracking, when monitored, then completion rate calculated (% completed vs started)
- [ ] Given completion rate, when displayed, then it's shown in dashboard
- [ ] Given trend analysis, when viewed, then completion rate trend over time is visible

**Technical Notes**:
- Metric: `completion_rate = completed_sessions / total_sessions`
- Track: started_at, completed_at (nullable)
- Dashboard: Show completion rate % and trend chart

**Definition of Done**:
- [ ] Completion tracking implemented
- [ ] Rate calculated correctly
- [ ] Dashboard updated
- [ ] Trend chart functional

**Dependencies**: US-031

---

### US-035: Drop-off Point Identification
**Epic**: EPIC-007  
**Priority**: Medium  
**Story Points**: 3  
**Status**: To Do  
**Sprint**: Sprint 13

**Story**:  
**As an** admin  
**I want** to identify where users drop off  
**So that** I can improve problematic questions

**Acceptance Criteria**:
- [ ] Given drop-off analysis, when viewed, then question-by-question dropout rates shown
- [ ] Given high dropout questions, when identified, then they're flagged for review
- [ ] Given insights, when generated, then recommendations provided

**Technical Notes**:
- Metric: `dropout_rate_per_question = dropouts_at_q / started_sessions`
- Flag: Questions with dropout_rate > 20%
- UI: Bar chart showing dropout rates

**Definition of Done**:
- [ ] Drop-off analysis implemented
- [ ] Rates calculated per question
- [ ] Flagging functional
- [ ] Visualization working

**Dependencies**: US-031, US-010

---

## Epic: EPIC-008 - Advanced Features (Sprint 19+)

### US-036: OpenAI Embedding Integration
**Epic**: EPIC-008  
**Priority**: Medium  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 19

**Story**:  
**As a** system  
**I want** to integrate OpenAI embeddings for free-text processing  
**So that** I can extract parameter insights from open-ended responses

**Acceptance Criteria**:
- [ ] Given OpenAI API key, when configured, then embeddings API accessible
- [ ] Given free-text response, when processed, then embedding vector generated
- [ ] Given embedding, when used, then regression head maps to parameter deltas
- [ ] Given error handling, when API fails, then graceful fallback implemented

**Technical Notes**:
- OpenAI SDK: `openai` Python package
- Embedding model: `text-embedding-3-small`
- Regression head: Simple MLP to map embedding → parameter deltas
- Cache: Store embeddings to reduce API calls

**Definition of Done**:
- [ ] OpenAI integration working
- [ ] Embeddings generated
- [ ] Regression head implemented
- [ ] Error handling robust

**Dependencies**: US-018

---

### US-037: Free-Text Response Processing
**Epic**: EPIC-008  
**Priority**: Medium  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 20

**Story**:  
**As a** user  
**I want** to answer free-text questions occasionally  
**So that** I can provide nuanced responses

**Acceptance Criteria**:
- [ ] Given free-text question, when displayed, then text input field shown
- [ ] Given response, when submitted, then text processed via embedding → regression → parameter update
- [ ] Given processing, when completed, then parameter vector updated appropriately
- [ ] Given unit tests, when run, then free-text processing validated

**Technical Notes**:
- Question type: `free_text`
- Processing: text → OpenAI embedding → regression head → parameter deltas → Bayesian update
- Limit: Only 1-2 free-text questions per session (to control costs)

**Definition of Done**:
- [ ] Free-text input component
- [ ] Processing pipeline working
- [ ] Parameter updates validated
- [ ] Cost monitoring implemented

**Dependencies**: US-036, US-018

---

### US-038: External API Integration
**Epic**: EPIC-008  
**Priority**: Low  
**Story Points**: 8  
**Status**: To Do  
**Sprint**: Sprint 25

**Story**:  
**As a** user  
**I want** links to real hobby opportunities from recommendations  
**So that** I can act on matches immediately

**Acceptance Criteria**:
- [ ] Given match result, when displayed, then external API queried for opportunities
- [ ] Given opportunities, when fetched, then links displayed in results
- [ ] Given API failure, when occurs, then graceful fallback (no links shown)
- [ ] Given caching, when implemented, then API calls minimized

**Technical Notes**:
- Example APIs: Eventbrite, Meetup, local hobby directories
- Abstract API layer: `HobbyOpportunityAPI` interface
- Caching: Store opportunities by location/archetype

**Definition of Done**:
- [ ] API integration working
- [ ] Links displayed in results
- [ ] Error handling robust
- [ ] Caching implemented

**Dependencies**: US-015

---

### US-039: Email Feedback Loop
**Epic**: EPIC-008  
**Priority**: Low  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 22

**Story**:  
**As a** system  
**I want** to collect user feedback via email  
**So that** I can measure match satisfaction

**Acceptance Criteria**:
- [ ] Given results page, when displayed, then optional email collection shown
- [ ] Given email submitted, when provided, then follow-up email sent after 7 days
- [ ] Given feedback survey, when responded, then satisfaction rating collected
- [ ] Given GDPR compliance, when implemented, then email deletion supported

**Technical Notes**:
- Email service: SendGrid or AWS SES
- Survey: Simple 1-5 satisfaction rating
- GDPR: DELETE endpoint removes email and responses

**Definition of Done**:
- [ ] Email collection working
- [ ] Follow-up emails sent
- [ ] Survey functional
- [ ] GDPR compliance verified

**Dependencies**: US-015

---

### US-040: Advanced Matching Features
**Epic**: EPIC-008  
**Priority**: Low  
**Story Points**: 5  
**Status**: To Do  
**Sprint**: Sprint 23

**Story**:  
**As a** system  
**I want** to apply min_requirements and contraindications in matching  
**So that** matches are more accurate

**Acceptance Criteria**:
- [ ] Given archetype, when matched, then min_requirements checked (hard thresholds)
- [ ] Given contraindications, when detected, then match disqualified if user vector violates
- [ ] Given filtering, when applied, then only qualified matches shown
- [ ] Given unit tests, when run, then filtering logic validated

**Technical Notes**:
- Min requirements: `user_vector[i] >= archetype.min_requirements[i]` for all i
- Contraindications: `user_vector[i] NOT IN archetype.contraindications[i]`
- Filter: Apply before cosine similarity ranking

**Definition of Done**:
- [ ] Requirements checking implemented
- [ ] Contraindications filtering working
- [ ] Filtering applied before ranking
- [ ] Unit tests passing

**Dependencies**: US-014

---

## Story Refinement Notes

### Refinement Session [TBD]
**Attendees**: PO, SM, Dev, QA, Arch

**Stories Reviewed**:
- [Stories to be refined during sprint planning]

**Action Items**:
- [ ] [Action items from refinement]

---

## Story Point Reference

| Points | Complexity | Effort | Examples |
|--------|------------|--------|----------|
| 1 | Trivial | < 2 hours | Simple config change, text update |
| 2 | Simple | 2-4 hours | Small feature, simple bug fix, seed data |
| 3 | Moderate | 4-8 hours | Standard feature with tests, API endpoint |
| 5 | Complex | 1-2 days | Feature requiring multiple components, UI component |
| 8 | Very Complex | 2-3 days | Large feature, significant refactoring, complex algorithm |

---

*Last Updated: 2025-01-27*
