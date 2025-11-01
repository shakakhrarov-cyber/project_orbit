# Product Backlog - ORBIT Project

## Backlog Overview
This document contains prioritized user stories and tasks for the ORBIT project. Items are organized by priority and mapped to sprints.

---

## Sprint 01 - High Priority (End-to-End MVP)

### US-001: Database Schema Setup
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-001

**Dependencies**: None

**Notes**: Foundation for all other features. Must be completed first.

---

### US-002: FastAPI Project Structure
**Priority**: High  
**Story Points**: 3  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-001

**Dependencies**: US-001

**Notes**: Enables API development

---

### US-004: Docker Compose Setup
**Priority**: High  
**Story Points**: 2  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-001

**Dependencies**: US-001, US-002

**Notes**: Critical for local development

---

### US-005: Question Display UI Component
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-002

**Dependencies**: US-002

**Notes**: Core user-facing component

---

### US-009: Seed 20 Questions from JSON
**Priority**: High  
**Story Points**: 2  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-003

**Dependencies**: US-001

**Notes**: Enables testing without full question bank

---

### US-010: Static Sequential Question Flow
**Priority**: High  
**Story Points**: 3  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-003

**Dependencies**: US-009, US-005

**Notes**: Core interview flow

---

### US-013: Seed 5 Archetypes with 10-Dim Vectors
**Priority**: High  
**Story Points**: 2  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-004

**Dependencies**: US-001

**Notes**: Enables matching testing

---

### US-014: Cosine Similarity Matching Algorithm
**Priority**: High  
**Story Points**: 3  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-004

**Dependencies**: US-013

**Notes**: Core matching logic

---

### US-015: Results Page with Recommendations
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 01  
**Status**: To Do  
**Epic**: EPIC-004

**Dependencies**: US-014, US-005

**Notes**: Completes MVP user journey

---

**Sprint 01 Total**: 30 points (adjustable based on capacity)

---

## Sprint 02 - High Priority (Complete MVP)

### US-003: Redis Session Caching
**Priority**: Medium  
**Story Points**: 2  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-001

**Dependencies**: US-002

---

### US-006: Response Collection (Multiple Types)
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-002

**Dependencies**: US-005, US-002

---

### US-011: Session State Management
**Priority**: High  
**Story Points**: 3  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-003

**Dependencies**: US-001, US-003, US-010

---

### US-012: Session Termination Logic
**Priority**: Medium  
**Story Points**: 2  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-003

**Dependencies**: US-010, US-011

---

### US-016: Match Explanation Generation
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-004

**Dependencies**: US-014, US-015

---

### US-008: Responsive Design (Mobile + Desktop)
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 02  
**Status**: To Do  
**Epic**: EPIC-002

**Dependencies**: US-005, US-006, US-007

---

**Sprint 02 Total**: 20 points

---

## Sprint 03-06 - Medium Priority (Adaptive Engine)

### US-017: Initialize User Parameter Vector
**Priority**: High  
**Story Points**: 2  
**Sprint**: Sprint 03  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-011

---

### US-018: Bayesian Parameter Update Logic
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 03  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-017

---

### US-019: Uncertainty Calculation (Covariance Tracking)
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 03  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-018

---

### US-023: Likert Answer Normalization
**Priority**: Medium  
**Story Points**: 2  
**Sprint**: Sprint 03  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-018

---

### US-020: Information Gain Calculation
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 04  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-019

---

### US-021: Question Selection Algorithm (Entropy-Based)
**Priority**: High  
**Story Points**: 8  
**Sprint**: Sprint 04-05  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-020, US-009

---

### US-022: Adaptive Session Termination
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 04  
**Status**: To Do  
**Epic**: EPIC-005

**Dependencies**: US-019, US-021

---

### US-025: Accessibility Support (Keyboard Nav, ARIA)
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 06  
**Status**: To Do  
**Epic**: EPIC-002

**Dependencies**: US-005, US-006

---

**Sprint 03-06 Total**: 33 points (distributed across sprints)

---

## Sprint 07-10 - Medium Priority (Admin Tools)

### US-026: Admin Authentication System
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 07  
**Status**: To Do  
**Epic**: EPIC-006

**Dependencies**: US-002

---

### US-027: Question CRUD Interface
**Priority**: High  
**Story Points**: 8  
**Sprint**: Sprint 08  
**Status**: To Do  
**Epic**: EPIC-006

**Dependencies**: US-026

---

### US-028: Question Parameter Targeting UI
**Priority**: Medium  
**Story Points**: 5  
**Sprint**: Sprint 08  
**Status**: To Do  
**Epic**: EPIC-006

**Dependencies**: US-027

---

### US-029: Archetype CRUD Interface
**Priority**: High  
**Story Points**: 8  
**Sprint**: Sprint 09  
**Status**: To Do  
**Epic**: EPIC-006

**Dependencies**: US-026

---

### US-030: Archetype Vector Editor
**Priority**: Medium  
**Story Points**: 5  
**Sprint**: Sprint 09  
**Status**: To Do  
**Epic**: EPIC-006

**Dependencies**: US-029

---

**Sprint 07-10 Total**: 31 points

---

## Sprint 11-14 - Medium Priority (Analytics)

### US-031: Metrics Collection System
**Priority**: High  
**Story Points**: 5  
**Sprint**: Sprint 11  
**Status**: To Do  
**Epic**: EPIC-007

**Dependencies**: US-011

---

### US-034: User Completion Rate Tracking
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 11  
**Status**: To Do  
**Epic**: EPIC-007

**Dependencies**: US-031

---

### US-032: Dashboard UI with Charts
**Priority**: High  
**Story Points**: 8  
**Sprint**: Sprint 12  
**Status**: To Do  
**Epic**: EPIC-007

**Dependencies**: US-031

---

### US-033: Question Performance Analysis
**Priority**: Medium  
**Story Points**: 5  
**Sprint**: Sprint 13  
**Status**: To Do  
**Epic**: EPIC-007

**Dependencies**: US-031, US-021

---

### US-035: Drop-off Point Identification
**Priority**: Medium  
**Story Points**: 3  
**Sprint**: Sprint 13  
**Status**: To Do  
**Epic**: EPIC-007

**Dependencies**: US-031, US-010

---

**Sprint 11-14 Total**: 24 points

---

## Sprint 19+ - Low Priority (Advanced Features)

### US-036: OpenAI Embedding Integration
**Priority**: Medium  
**Story Points**: 5  
**Sprint**: Sprint 19  
**Status**: To Do  
**Epic**: EPIC-008

**Dependencies**: US-018

---

### US-037: Free-Text Response Processing
**Priority**: Medium  
**Story Points**: 8  
**Sprint**: Sprint 20  
**Status**: To Do  
**Epic**: EPIC-008

**Dependencies**: US-036, US-018

---

### US-039: Email Feedback Loop
**Priority**: Low  
**Story Points**: 5  
**Sprint**: Sprint 22  
**Status**: To Do  
**Epic**: EPIC-008

**Dependencies**: US-015

---

### US-040: Advanced Matching Features
**Priority**: Low  
**Story Points**: 5  
**Sprint**: Sprint 23  
**Status**: To Do  
**Epic**: EPIC-008

**Dependencies**: US-014

---

### US-038: External API Integration
**Priority**: Low  
**Story Points**: 8  
**Sprint**: Sprint 25  
**Status**: To Do  
**Epic**: EPIC-008

**Dependencies**: US-015

---

**Sprint 19+ Total**: 31 points

---

## Technical Debt

### TD-001: Refactor Static Flow to Adaptive Flow
**Description**: The static sequential question flow (US-010) needs refactoring to integrate with adaptive engine (US-021) in Sprint 03

**Impact**: Medium  
**Effort**: Medium  
**Priority**: Medium  
**Sprint**: Sprint 03

**Rationale**: Static flow was built first to validate matching logic, but adaptive engine requires different question selection logic

**Proposed Solution**: Extract question selection logic into service layer, swap static selector for adaptive selector

---

### TD-002: Add Free-Text Processing
**Description**: Free-text questions are deferred to Phase 3, but architecture should support them

**Impact**: Low  
**Effort**: Small  
**Priority**: Low  
**Sprint**: Sprint 19+

**Rationale**: Free-text processing requires OpenAI API and regression head training

**Proposed Solution**: Design response processing interface to support both Likert and free-text

---

### TD-003: Optimize Matching Performance
**Description**: Cosine similarity for 50+ archetypes may need optimization

**Impact**: Low  
**Effort**: Small  
**Priority**: Low  
**Sprint**: Sprint 07+

**Rationale**: Current implementation sufficient for 5-10 archetypes, may need vectorization for scale

**Proposed Solution**: Use NumPy vectorized operations, consider caching similarity scores

---

## Bugs

_None yet - project starting Sprint 01_

---

## Backlog Statistics

- **Total Stories**: 40
- **Estimated Points**: 169
- **High Priority (Sprint 01-02)**: 12 stories, 50 points
- **Medium Priority (Sprint 03-14)**: 19 stories, 89 points
- **Low Priority (Sprint 19+)**: 5 stories, 31 points
- **Technical Debt Items**: 3
- **Open Bugs**: 0

### Sprint Capacity Estimate
- **Sprint 01**: 18-21 points (realistic for 1 week)
- **Sprint 02**: 15-20 points
- **Sprint 03-06**: 5-8 points per sprint (adaptive engine complexity)
- **Sprint 07+**: 15-20 points per sprint

---

## Prioritization Rationale

### Sprint 01 Focus
- **Goal**: End-to-end MVP demonstrating core value
- **Stories Selected**: Foundation (database, API) + Static flow + Basic matching
- **Rationale**: Validate approach before investing in adaptive complexity

### Sprint 02 Focus
- **Goal**: Polish MVP, add missing features
- **Stories Selected**: Session management, responsive design, explanations
- **Rationale**: Complete MVP before moving to adaptive engine

### Sprint 03-06 Focus
- **Goal**: Implement adaptive engine incrementally
- **Stories Selected**: Bayesian updates → Information gain → Question selection
- **Rationale**: Build complexity incrementally with testing at each step

### Sprint 07+ Focus
- **Goal**: Enable production readiness and scaling
- **Stories Selected**: Admin tools, analytics, advanced features
- **Rationale**: Support long-term operations and optimization

---

*Last Updated: 2025-01-27*
