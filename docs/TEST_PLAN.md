# Test Plan

## Test Strategy

### Testing Objectives
1. Ensure all features meet acceptance criteria
2. Maintain high code quality and test coverage
3. Prevent regressions
4. Validate performance and scalability
5. Ensure security requirements are met

### Testing Scope
**In Scope:**
- Functional testing
- Integration testing
- Unit testing
- Regression testing
- Performance testing
- Security testing

**Out of Scope:**
- [Items explicitly not tested]

## Test Levels

### 1. Unit Testing
**Goal**: Test individual functions/methods in isolation

**Coverage Target**: 80% minimum

**Responsibilities**: Developers

**Tools**: pytest (Python), Jest (JavaScript)

**Approach**:
- Test each function independently
- Mock external dependencies (database, Redis, OpenAI API)
- Test edge cases and error conditions
- Run automatically on commit

**ORBIT-Specific Unit Tests**:
- `test_cosine_similarity()`: Validate cosine similarity calculation for 10-dim vectors
- `test_bayesian_update()`: Validate Bayesian parameter update math
- `test_uncertainty_calculation()`: Validate covariance-based uncertainty
- `test_information_gain()`: Validate entropy reduction calculation
- `test_likert_normalization()`: Validate Likert scale → 0-1 mapping
- `test_question_selection()`: Validate adaptive question selection logic
- `test_vector_operations()`: Validate NumPy vector math utilities

### 2. Integration Testing
**Goal**: Test interactions between components

**Coverage Target**: Key integration points

**Responsibilities**: Developers + QA

**Tools**: pytest with FastAPI TestClient, pytest-asyncio

**Approach**:
- Test API endpoints with FastAPI TestClient
- Test database interactions (SQLAlchemy models, migrations)
- Test Redis cache integration
- Test external service integrations (OpenAI API mocking)
- Run automatically in CI/CD

**ORBIT-Specific Integration Tests**:
- `test_session_creation()`: POST /session/start creates session and returns question
- `test_response_submission()`: POST /response updates session and returns next question
- `test_session_termination()`: Session terminates after 40 questions or 20 minutes
- `test_result_generation()`: GET /result returns top 3 matches with cosine similarity
- `test_redis_cache()`: Session state cached and retrieved correctly
- `test_database_models()`: All entities persist and query correctly

### 3. End-to-End Testing
**Goal**: Test complete user workflows

**Coverage Target**: Critical user paths

**Responsibilities**: QA

**Tools**: Playwright or Cypress

**Approach**:
- Test complete user journeys (start → answer → results)
- Validate UI interactions (question display, response submission)
- Test cross-browser compatibility (Chrome, Firefox, Safari)
- Run on staging environment

**ORBIT-Specific E2E Tests**:
- `test_complete_interview_flow()`: User completes 20-question session and sees results
- `test_question_display()`: Question renders correctly, no progress indicators visible
- `test_result_display()`: Top 3 matches displayed with fit scores and explanations
- `test_responsive_design()`: Interface works on mobile and desktop
- `test_session_persistence()`: Session state persists across page refreshes

### 4. Performance Testing
**Goal**: Validate system performance under load

**Responsibilities**: QA + Architect

**Tools**: [Performance testing tools]

**Metrics**:
- Response time: < 200ms for question selection API
- Response time: < 100ms for matching algorithm (50 archetypes)
- Throughput: 100 requests/second per API instance
- Concurrent users: 1000 active sessions
- Resource utilization: CPU < 70%, Memory < 80%

### 5. Security Testing
**Goal**: Identify security vulnerabilities

**Responsibilities**: QA + Architect

**Approach**:
- Input validation testing
- Authentication/authorization testing
- SQL injection testing
- XSS testing
- Dependency vulnerability scanning

## Test Environment

### Development
- Local development machines
- Unit and basic integration tests

### Staging
- Mirror of production
- Full integration and E2E testing
- Performance testing

### Production
- Live system
- Smoke tests after deployment
- Monitoring and real-time validation

## Test Cases

### Feature: Session Management

#### TC-001: Session Creation Returns First Question
**Priority**: High  
**Type**: Integration

**Preconditions**:
- Database seeded with 20 questions
- API server running
- Redis cache available

**Test Steps**:
1. POST /session/start
2. Verify response contains question object
3. Verify session created in database
4. Verify session cached in Redis

**Expected Result**:
- Status code 200
- Response includes question_id, question_text, question_type
- Session record exists in database
- Session cached in Redis

**Acceptance Criteria**:
- [ ] Session created successfully
- [ ] First question returned
- [ ] Cache working

---

#### TC-002: Response Submission Updates Session
**Priority**: High  
**Type**: Integration

**Preconditions**:
- Active session exists
- Question displayed to user

**Test Steps**:
1. POST /response with session_id and answer
2. Verify session updated (answered_qids array)
3. Verify next question returned (or done flag)
4. Verify cache updated

**Expected Result**:
- Status code 200
- Session answered_qids includes question_id
- Next question returned OR done flag set
- Cache reflects updated state

**Acceptance Criteria**:
- [ ] Session updated correctly
- [ ] Next question returned
- [ ] Cache synchronized

---

### Feature: Matching Engine

#### TC-003: Cosine Similarity Calculation Accuracy
**Priority**: High  
**Type**: Unit

**Preconditions**:
- NumPy available
- Test vectors defined

**Test Steps**:
1. Create test user vector [0.5, 0.5, ..., 0.5]
2. Create test archetype vector [0.8, 0.8, ..., 0.8]
3. Compute cosine similarity
4. Verify result matches expected value (≈ 1.0)

**Expected Result**:
- Cosine similarity = 1.0 (identical vectors)
- Calculation handles 10-dimensional vectors
- Performance < 1ms

**Acceptance Criteria**:
- [ ] Math validated correctly
- [ ] Handles edge cases (zero vectors)
- [ ] Performance acceptable

---

#### TC-004: Match Ranking Correctness
**Priority**: High  
**Type**: Integration

**Preconditions**:
- 5 archetypes seeded
- User vector computed from responses

**Test Steps**:
1. Compute cosine similarity for all archetypes
2. Rank by similarity (highest first)
3. Verify top 3 matches returned
4. Verify ranking order correct

**Expected Result**:
- Top 3 matches returned
- Ranked by similarity (highest fit score first)
- Fit scores between 0-1

**Acceptance Criteria**:
- [ ] Ranking algorithm working
- [ ] Top 3 matches correct
- [ ] Fit scores valid

---

### Feature: Adaptive Engine (Sprint 03+)

#### TC-005: Bayesian Parameter Update
**Priority**: High  
**Type**: Unit

**Preconditions**:
- Prior mean and covariance defined
- Likert response normalized

**Test Steps**:
1. Initialize prior: mean=[0.5]*10, cov=0.25²*I
2. Apply Bayesian update with observation
3. Verify posterior mean updated
4. Verify posterior covariance reduced

**Expected Result**:
- Posterior mean reflects observation
- Covariance reduced (uncertainty decreased)
- Math validated against scipy.stats

**Acceptance Criteria**:
- [ ] Bayesian update correct
- [ ] Uncertainty decreases
- [ ] Unit tests passing

---

#### TC-006: Information Gain Calculation
**Priority**: High  
**Type**: Unit

**Preconditions**:
- Current covariance matrix
- Question with targets and weights

**Test Steps**:
1. Compute current uncertainty (mean of diagonal)
2. Compute expected information gain for question
3. Verify higher gain = more informative
4. Verify gain calculation matches formula

**Expected Result**:
- Information gain > 0 for informative questions
- Gain calculation accurate
- Performance < 10ms per question

**Acceptance Criteria**:
- [ ] Gain calculation correct
- [ ] Ranking by gain works
- [ ] Performance acceptable

---

#### TC-007: Question Selection Algorithm
**Priority**: High  
**Type**: Integration

**Preconditions**:
- Active session with parameter vector
- Question bank with 20+ questions
- Some questions already answered

**Test Steps**:
1. Identify parameters with highest uncertainty
2. Retrieve candidate questions targeting those parameters
3. Compute information gain for each candidate
4. Select highest-gain question (subject to constraints)
5. Verify selected question not already answered

**Expected Result**:
- Question selected targets high-uncertainty parameters
- Selected question has high information gain
- Diversity constraint applied (no repetitive questions)
- Performance < 100ms

**Acceptance Criteria**:
- [ ] Selection algorithm working
- [ ] Questions not repeated
- [ ] Performance acceptable

---

### Feature: Session Termination

#### TC-008: Session Terminates After 40 Questions
**Priority**: Medium  
**Type**: Integration

**Preconditions**:
- Active session with 39 questions answered

**Test Steps**:
1. Submit 40th response
2. Verify done flag returned
3. Verify session marked complete
4. Verify results can be generated

**Expected Result**:
- Response includes {"done": true}
- No next question returned
- Session status = "completed"
- Results endpoint accessible

**Acceptance Criteria**:
- [ ] Termination logic working
- [ ] Session marked complete
- [ ] Results accessible

---

#### TC-009: Session Terminates After 20 Minutes
**Priority**: Medium  
**Type**: Integration

**Preconditions**:
- Active session created 20+ minutes ago
- Less than 40 questions answered

**Test Steps**:
1. Attempt to submit response
2. Verify done flag returned
3. Verify time-based termination

**Expected Result**:
- Response includes {"done": true}
- Termination reason = "time_limit"
- Session marked complete

**Acceptance Criteria**:
- [ ] Time limit enforced
- [ ] Session terminated correctly
- [ ] Edge cases handled

---

### Feature: Results Display

#### TC-010: Results Page Displays Top 3 Matches
**Priority**: High  
**Type**: E2E

**Preconditions**:
- Completed session
- Match results computed

**Test Steps**:
1. Navigate to results page
2. Verify top 3 matches displayed
3. Verify fit scores shown (0-1 range)
4. Verify explanations displayed

**Expected Result**:
- 3 matches displayed
- Rank, name, fit score, explanation visible
- Layout responsive and accessible

**Acceptance Criteria**:
- [ ] Results display correctly
- [ ] Explanations readable
- [ ] UI meets design principles

---

## Defect Management

### Severity Levels
- **Critical**: System crash, data loss, security breach
- **Major**: Major functionality broken, no workaround
- **Minor**: Minor functionality issue, workaround exists
- **Trivial**: Cosmetic issues

### Defect Lifecycle
1. New → Assigned → In Progress → Fixed → Testing → Closed
2. Can be Reopened if fix doesn't work

## Test Metrics

### Tracked Metrics
- Test execution rate
- Test pass/fail rate
- Defect density
- Defect resolution time
- Code coverage percentage
- Regression rate

### Quality Gates
- All critical/major bugs resolved
- 80%+ unit test coverage
- All E2E tests passing
- Performance benchmarks met
- Security scan passes

## Regression Testing

### Regression Suite
- Core functionality tests
- Previously fixed bug tests
- Critical path tests

### Trigger Events
- Before each release
- After major refactoring
- After dependency updates

## Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

## Test Schedule

### Sprint Testing Schedule
- **Day 1-2**: Review stories, create test cases
- **Day 3-8**: Continuous testing as features complete
- **Day 9**: Regression testing
- **Day 10**: Final validation and sprint demo prep

---

*Last Updated: [Date]*

