# Product Roadmap - ORBIT

## Vision
Build a web-based adaptive interview system that unobtrusively collects behavioral and preference data from users to generate accurate, bias-free hobby or role matches. Replace static psychometric tests with a dynamic, context-aware system that learns about users in real time through conversational questions.

## Mission Statement
ORBIT solves the problem of finding relevant hobbies or roles that match a user's true preferences and constraints. Traditional questionnaires are static, long, and often biased. ORBIT uses adaptive questioning powered by Bayesian inference to efficiently converge on accurate matches while maintaining a neutral, conversational user experience.

**Target Users**: Individuals seeking new hobbies, career guidance, or role matching based on preferences and constraints.

## Strategic Goals
1. **Goal 1**: Build a production-ready adaptive interview system that converges to reliable results in <40 questions
2. **Goal 2**: Achieve >80% user completion rate and >4/5 satisfaction rating
3. **Goal 3**: Enable non-technical admins to manage questions and archetypes without developer intervention

---

## Quarters / Milestones

### Q1 2025 - Prototype (Phase 1)
**Theme**: Foundation & MVP Core Functionality

**Duration**: 4-6 weeks (Sprint 01-06)

**Objectives:**
- [ ] Build end-to-end MVP with static questionnaire flow
- [ ] Implement basic matching engine with cosine similarity
- [ ] Develop adaptive engine with Bayesian inference and entropy-based question selection
- [ ] Seed system with 20-30 questions and 10 archetypes

**Key Results:**
- KR1: End-to-end user flow working (static → adaptive transition)
- KR2: Average questions to confidence < 35
- KR3: Local CSV/JSON data storage functional

**Epics:**
- EPIC-001: Core Infrastructure & Data Model
- EPIC-002: Front-End User Interface
- EPIC-003: Static Interview Flow (MVP)
- EPIC-004: Basic Matching Engine (MVP)
- EPIC-005: Adaptive Engine (Bayesian Inference)

---

### Q2 2025 - MVP (Phase 2)
**Theme**: Production Readiness & Admin Tools

**Duration**: 8-12 weeks (Sprint 07-18)

**Objectives:**
- [ ] Migrate to cloud database (PostgreSQL/Firestore)
- [ ] Build admin panel for question authoring and archetype management
- [ ] Implement analytics dashboard for question performance
- [ ] Add email-based feedback loop
- [ ] Scale to 100+ questions and 50+ archetypes

**Key Results:**
- KR1: Admin can add/edit questions without developer intervention
- KR2: Question performance metrics tracked and visualized
- KR3: User completion rate > 80%
- KR4: Match satisfaction > 4/5 (from post-survey)

**Epics:**
- EPIC-006: Admin Tools
- EPIC-007: Analytics & Metrics Dashboard
- EPIC-008: Advanced Features (partial)

---

### Q3 2025 - Beta Launch (Phase 3)
**Theme**: Scale & Integration

**Duration**: 3 months (Sprint 19-30)

**Objectives:**
- [ ] Integrate with event APIs or hobby directories
- [ ] Add free-text processing with OpenAI embeddings
- [ ] Implement advanced matching features
- [ ] Collect calibration data from 100+ users
- [ ] Achieve engine stability (test/retest correlation > 0.85)

**Key Results:**
- KR1: 100+ questions and 50+ archetypes in production
- KR2: Integration with external hobby/event APIs
- KR3: Retention rate > 50% (users engaged after 30 days)
- KR4: Engine stability correlation > 0.85

**Epics:**
- EPIC-008: Advanced Features (complete)
- EPIC-009: Integration & Scaling (if needed)

---

## Success Metrics

### Core Metrics (from PRD Section 11)
- **Average questions to confidence**: Mean count until threshold reached - Target: < 35 questions
- **User completion rate**: % users completing session - Target: > 80%
- **Match satisfaction**: Post-survey rating of accuracy - Target: > 4/5
- **Retention rate**: % users still engaged with hobby after 30 days - Target: > 50%
- **Engine stability**: Correlation of vector between test/retest - Target: > 0.85

### Technical Metrics
- **API response time**: < 200ms for question selection
- **Session state persistence**: 100% reliability
- **Test coverage**: > 80% unit test coverage
- **Database query performance**: < 50ms for archetype matching

### Business Metrics
- **Question bank size**: Scale from 20 → 100+ questions
- **Archetype library size**: Scale from 10 → 50+ archetypes
- **Admin efficiency**: < 5 minutes to add/edit question

---

## Assumptions & Dependencies

### Assumptions
- **Assumption 1**: Users will engage with conversational interface without visible progress indicators
- **Assumption 2**: 10-dimensional parameter vector sufficiently captures user preferences
- **Assumption 3**: Bayesian inference provides better convergence than static questionnaires
- **Assumption 4**: OpenAI API will be available and cost-effective for text embeddings

### Dependencies
- **Dependency 1**: OpenAI API access for text embedding (free-text processing)
- **Dependency 2**: PostgreSQL/Firestore cloud database availability
- **Dependency 3**: External hobby/event APIs for Phase 3 integration
- **Dependency 4**: Content team/Product Owner for question authoring (per user choice)

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **User fatigue from long sessions** | High | Dynamic question capping & entropy-based stop condition |
| **Ambiguity in free-text parsing** | Medium | Limit open-ended questions to reflection only; use OpenAI embeddings |
| **Overfitting to small pilot dataset** | Medium | Collect calibration data from 100+ users before v1 release |
| **Misinterpretation of recommendations** | Medium | Provide transparent reasoning in final report |
| **Bayesian inference complexity** | Medium | Start with static flow, add adaptation incrementally |
| **Docker/setup complexity** | Low | Use simple docker-compose.yml; document setup thoroughly |

---

## Development Phases Alignment

### Phase 1 - Prototype (4-6 weeks)
**Sprints**: 01-06  
**Focus**: Core adaptive interview loop, basic matching, local data storage

### Phase 2 - MVP (8-12 weeks)  
**Sprints**: 07-18  
**Focus**: Cloud database, admin panel, analytics, production deployment

### Phase 3 - Beta Launch (3 months)
**Sprints**: 19-30  
**Focus**: Scale, integration, advanced features, user calibration

---

*Last Updated: 2025-01-27*

