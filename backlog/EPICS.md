# Epics - ORBIT Project

## What is an Epic?
An epic is a large body of work that can be broken down into multiple user stories. Epics typically span multiple sprints and represent significant features or initiatives.

---

## EPIC-001: Core Infrastructure & Data Model

**Goal**: Establish the foundational database schema, API structure, and development environment to support the adaptive interview system.

**Business Value**: Enables all other features. Without proper data modeling and infrastructure, the system cannot function.

**Target Quarter**: Q1 2025

**Status**: Not Started

### Success Metrics
- Database schema supports all entities (User, Session, Question, Response, Archetype, MatchReport)
- API foundation ready for front-end integration
- Docker Compose setup allows developers to run system locally
- Redis session caching reduces database load

### User Stories
- [ ] US-001: Database schema setup - 5 points
- [ ] US-002: FastAPI project structure - 3 points
- [ ] US-003: Redis session caching - 2 points
- [ ] US-004: Docker Compose setup - 2 points

**Total Story Points**: 12

### Dependencies
- None (foundational epic)

### Risks
- **Risk**: Docker setup complexity may delay development start
- **Mitigation**: Use simple docker-compose.yml with clear documentation

### Timeline
- **Start Date**: Sprint 01
- **Target Completion**: Sprint 02
- **Actual Completion**: [TBD]

---

## EPIC-002: Front-End User Interface

**Goal**: Build a clean, minimalist conversational interface that displays one question at a time and collects user responses without revealing adaptive logic.

**Business Value**: The user-facing experience determines engagement and completion rates. Must be neutral, accessible, and responsive.

**Target Quarter**: Q1 2025

**Status**: Not Started

### Success Metrics
- Users can answer questions without seeing progress indicators
- Interface works on mobile and desktop
- Accessibility score > 90 (WCAG AA compliance)
- Response time < 100ms for UI interactions

### User Stories
- [ ] US-005: Question display UI component - 5 points
- [ ] US-006: Response collection (multiple-choice, Likert, slider) - 5 points
- [ ] US-007: Results page with recommendations - 5 points
- [ ] US-008: Responsive design (mobile + desktop) - 3 points
- [ ] US-025: Accessibility support (keyboard nav, ARIA) - 3 points

**Total Story Points**: 21

### Dependencies
- EPIC-001: Requires API endpoints to be ready

### Risks
- **Risk**: Over-engineering UI before core functionality works
- **Mitigation**: Start with minimal UI, enhance iteratively

### Timeline
- **Start Date**: Sprint 01
- **Target Completion**: Sprint 03
- **Actual Completion**: [TBD]

---

## EPIC-003: Static Interview Flow (MVP)

**Goal**: Implement a non-adaptive questionnaire flow that allows users to answer questions sequentially, demonstrating end-to-end functionality before adding Bayesian adaptation.

**Business Value**: Validates core matching logic and user experience before investing in complex adaptive algorithms.

**Target Quarter**: Q1 2025

**Status**: Not Started

### Success Metrics
- Users can complete a 20-question session
- Session state persists correctly
- Session terminates after 40 questions or 20 minutes
- Question flow displays correctly without adaptation logic

### User Stories
- [ ] US-009: Seed 20 questions from JSON - 2 points
- [ ] US-010: Static sequential question flow - 3 points
- [ ] US-011: Session state management - 3 points
- [ ] US-012: Session termination logic (time/limit based) - 2 points

**Total Story Points**: 10

### Dependencies
- EPIC-001: Database and API must be ready
- EPIC-002: UI components needed for question display

### Risks
- **Risk**: Static flow may need refactoring when adding adaptation
- **Mitigation**: Design session state management to be extensible

### Timeline
- **Start Date**: Sprint 01
- **Target Completion**: Sprint 02
- **Actual Completion**: [TBD]

---

## EPIC-004: Basic Matching Engine (MVP)

**Goal**: Implement cosine similarity-based matching between user parameter vectors and predefined archetypes, generating 2-3 recommendations with explanations.

**Business Value**: Core value proposition - users get personalized recommendations based on their answers.

**Target Quarter**: Q1 2025

**Status**: Not Started

### Success Metrics
- Cosine similarity calculation accurate (unit tested)
- Top 3 matches displayed with fit scores
- Explanations provided for each match
- Matching completes in < 100ms

### User Stories
- [ ] US-013: Seed 5 archetypes with 10-dim vectors - 2 points
- [ ] US-014: Cosine similarity matching algorithm - 3 points
- [ ] US-015: Results page with recommendations - 5 points
- [ ] US-016: Match explanation generation - 3 points

**Total Story Points**: 13

### Dependencies
- EPIC-001: Database needed for archetype storage
- EPIC-003: User vector needed from session responses

### Risks
- **Risk**: Simple cosine similarity may not capture all nuances
- **Mitigation**: Start simple, iterate based on user feedback

### Timeline
- **Start Date**: Sprint 01
- **Target Completion**: Sprint 02
- **Actual Completion**: [TBD]

---

## EPIC-005: Adaptive Engine (Bayesian Inference)

**Goal**: Implement Bayesian parameter updates and entropy-based question selection to dynamically adapt the interview flow based on user responses.

**Business Value**: Differentiates ORBIT from static questionnaires. Reduces questions needed while improving accuracy.

**Target Quarter**: Q1 2025

**Status**: Not Started

### Success Metrics
- Average questions to confidence < 35
- Parameter vector convergence validated (test/retest correlation > 0.85)
- Question selection algorithm reduces uncertainty efficiently
- Information gain calculation accurate

### User Stories
- [ ] US-017: Initialize user parameter vector (0.5 ± 0.25) - 2 points
- [ ] US-018: Bayesian parameter update logic - 5 points
- [ ] US-019: Uncertainty calculation (covariance tracking) - 5 points
- [ ] US-020: Information gain calculation - 5 points
- [ ] US-021: Question selection algorithm (entropy-based) - 8 points
- [ ] US-022: Adaptive session termination (< 0.12 uncertainty) - 3 points
- [ ] US-023: Likert answer normalization - 2 points

**Total Story Points**: 30

### Dependencies
- EPIC-003: Static flow must work first
- EPIC-004: Basic matching validates the approach

### Risks
- **Risk**: Bayesian inference complexity may introduce bugs
- **Mitigation**: Comprehensive unit tests, mathematical validation
- **Risk**: May not converge faster than static flow initially
- **Mitigation**: Calibrate with pilot data from 100+ users

### Timeline
- **Start Date**: Sprint 03
- **Target Completion**: Sprint 06
- **Actual Completion**: [TBD]

---

## EPIC-006: Admin Tools

**Goal**: Build interfaces for non-technical admins to author questions, manage archetypes, and configure the system without developer intervention.

**Business Value**: Enables content team to scale question bank and archetype library independently.

**Target Quarter**: Q2 2025

**Status**: Not Started

### Success Metrics
- Admin can add/edit question in < 5 minutes
- Question authoring interface intuitive (no training required)
- Archetype editor supports vector editing and validation
- Admin authentication and authorization working

### User Stories
- [ ] US-026: Admin authentication system - 5 points
- [ ] US-027: Question CRUD interface - 8 points
- [ ] US-028: Question parameter targeting UI - 5 points
- [ ] US-029: Archetype CRUD interface - 8 points
- [ ] US-030: Archetype vector editor - 5 points

**Total Story Points**: 31

### Dependencies
- EPIC-001: Database and API foundation
- EPIC-002: Front-end components can be reused

### Risks
- **Risk**: Complex admin UI may be over-engineered
- **Mitigation**: Start with simple forms, iterate based on admin feedback

### Timeline
- **Start Date**: Sprint 07
- **Target Completion**: Sprint 10
- **Actual Completion**: [TBD]

---

## EPIC-007: Analytics & Metrics Dashboard

**Goal**: Track system performance, question effectiveness, user metrics, and provide insights for continuous improvement.

**Business Value**: Data-driven optimization of questions and matching algorithm improves user satisfaction and completion rates.

**Target Quarter**: Q2 2025

**Status**: Not Started

### Success Metrics
- Metrics dashboard displays all KPIs from PRD Section 11
- Question performance analytics available
- Drop-off points identified and visualized
- Average question count tracked per session

### User Stories
- [ ] US-031: Metrics collection system - 5 points
- [ ] US-032: Dashboard UI with charts - 8 points
- [ ] US-033: Question performance analysis - 5 points
- [ ] US-034: User completion rate tracking - 3 points
- [ ] US-035: Drop-off point identification - 3 points

**Total Story Points**: 24

### Dependencies
- EPIC-001: Database needed for metrics storage
- EPIC-006: Admin tools provide context for analytics

### Risks
- **Risk**: Over-tracking metrics may slow system
- **Mitigation**: Use async logging, batch processing

### Timeline
- **Start Date**: Sprint 11
- **Target Completion**: Sprint 14
- **Actual Completion**: [TBD]

---

## EPIC-008: Advanced Features (Phase 3)

**Goal**: Integrate free-text processing, external APIs, feedback loops, and advanced matching features for beta launch.

**Business Value**: Expands system capabilities and enables real-world integration with hobby directories and event APIs.

**Target Quarter**: Q3 2025

**Status**: Not Started

### Success Metrics
- Free-text questions processed with OpenAI embeddings
- Integration with 1+ external API (event/hobby directory)
- Email feedback loop operational
- Retention rate > 50% (users engaged after 30 days)

### User Stories
- [ ] US-036: OpenAI embedding integration - 5 points
- [ ] US-037: Free-text response processing - 8 points
- [ ] US-038: External API integration (events/hobbies) - 8 points
- [ ] US-039: Email feedback loop - 5 points
- [ ] US-040: Advanced matching features (contraindications) - 5 points

**Total Story Points**: 31

### Dependencies
- EPIC-005: Adaptive engine must be stable
- External APIs: Requires API access and keys

### Risks
- **Risk**: OpenAI API costs may be high
- **Mitigation**: Limit free-text questions, cache embeddings
- **Risk**: External API changes may break integration
- **Mitigation**: Abstract API layer, version handling

### Timeline
- **Start Date**: Sprint 19
- **Target Completion**: Sprint 30
- **Actual Completion**: [TBD]

---

## Epic Prioritization

| Epic ID | Title | Business Value | Effort | Priority Score | Status |
|---------|-------|----------------|--------|----------------|--------|
| EPIC-001 | Core Infrastructure | Critical | Medium | Critical | Not Started |
| EPIC-002 | Front-End UI | High | Large | High | Not Started |
| EPIC-003 | Static Interview Flow | High | Small | High | Not Started |
| EPIC-004 | Basic Matching Engine | Critical | Medium | Critical | Not Started |
| EPIC-005 | Adaptive Engine | High | Very Large | Medium | Not Started |
| EPIC-006 | Admin Tools | Medium | Large | Medium | Not Started |
| EPIC-007 | Analytics Dashboard | Medium | Medium | Medium | Not Started |
| EPIC-008 | Advanced Features | Low | Very Large | Low | Not Started |

**Priority Score Formula**: Business Value / Effort

**Execution Order**: EPIC-001 → EPIC-002 → EPIC-003 → EPIC-004 → EPIC-005 → EPIC-006 → EPIC-007 → EPIC-008

---

## Completed Epics

_None yet - project starting Sprint 01_

---

*Last Updated: 2025-01-27*
