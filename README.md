# 🧭 Agile Scrum Framework for Cursor with AI Agents

This repository defines a conceptual **Agile Scrum framework** tailored for **software development with AI agents** inside **Cursor**.

---

## 🚀 Overview

AI agents collaborate as a virtual Scrum team to plan, develop, test, and review software projects. Each agent assumes a role (Product Owner, Scrum Master, Developer, QA, Architect) while you act as **Chief Engineer / Project Owner**.

This system ensures consistent velocity, documentation, and high-quality code through an agent-driven Scrum process.

---

## 🧱 Folder Structure

```
/.agents/
  product_owner.prompt.md
  scrum_master.prompt.md
  developer.prompt.md
  qa.prompt.md
  architect.prompt.md

/docs/
  ROADMAP.md
  ARCH_NOTES.md
  TEST_PLAN.md

/sprints/
  SPRINT_01/
    SPRINT_PLAN.md
    DAILY_LOG.md
    SPRINT_REVIEW.md
    RETRO.md

/backlog/
  BACKLOG.md
  EPICS.md
  USER_STORIES.md
```

---

## 🧩 Agent Role Prompts

### **Product Owner (PO Agent)**
**Goal:** Maintain clarity of vision and translate it into actionable backlog items.
```markdown
You are the Product Owner. Review `ROADMAP.md` and `BACKLOG.md`.  
For each high-level epic, break it into user stories following the INVEST model.  
Prioritize by business value and development feasibility.  
Output a refined backlog with acceptance criteria.
```

### **Scrum Master (SM Agent)**
**Goal:** Maintain sprint cadence and process discipline.
```markdown
You are the Scrum Master. Review `SPRINT_PLAN.md` and `DAILY_LOG.md`.  
Identify blockers, suggest reassignments, and summarize updates for today's stand-up.  
Output: concise update with **Progress**, **Blockers**, **Next Steps**.
```

### **Developer (Dev Agent)**
**Goal:** Implement features and ensure technical quality.
```markdown
You are the Developer. Implement tasks listed in `SPRINT_PLAN.md`.  
Follow clean architecture principles, document code inline, and generate concise PR descriptions.  
Verify functionality against acceptance criteria before submitting.
```

### **QA / Test Engineer (QA Agent)**
**Goal:** Maintain high code quality and documentation clarity.
```markdown
You are the QA Engineer. Review latest commits.  
Write or update test cases, check linting, and run integration tests.  
Summarize results in `TEST_REPORT.md` and flag regressions.
```

### **Architect (Arch Agent)**
**Goal:** Maintain architectural consistency and scalability.
```markdown
You are the Architect. Review new features for design coherence.  
Suggest refactors, dependency graph changes, or data flow improvements.  
Document architectural changes in `ARCH_NOTES.md`.
```

---

## ⚙️ Sprint Lifecycle

| Phase | Owner | AI Role | Deliverables |
|-------|--------|---------|---------------|
| **Backlog Grooming** | PO + Arch | Suggests epics, decomposes stories | `BACKLOG.md` updated |
| **Sprint Planning** | PO + SM | Converts stories → tasks | `SPRINT_PLAN.md` |
| **Development** | Dev + Arch | Builds features, commits code | Code + Tests |
| **Daily Sync** | SM | Summarizes progress, flags blockers | `DAILY_LOG.md` |
| **Review & Demo** | PO | Summarizes sprint results | `SPRINT_REVIEW.md` |
| **Retrospective** | SM | Generates improvement summary | `RETRO.md` |

---

## 🧠 Example Interaction Flow

1. **You:** `@ProductOwner, refine backlog based on user feedback.`  
   → Updates `BACKLOG.md` with new user stories.

2. **You:** `@ScrumMaster, plan next sprint with top 5 backlog items.`  
   → Generates `SPRINT_PLAN.md` with story points & goals.

3. **You:** `@Developer, implement feature #3.`  
   → Writes and commits code per acceptance criteria.

4. **@QA:** Runs tests, updates `TEST_REPORT.md`.

5. **@Architect:** Reviews structure, updates `ARCH_NOTES.md`.

---

## 📊 Metrics & Continuous Improvement

Track and visualize progress via automated metrics:
- **Velocity:** Story points per sprint
- **Lead Time:** Time from To Do → Done
- **Defect Rate:** Failed QA tests / sprint
- **Backlog Churn:** % of tasks added mid-sprint
- **Satisfaction:** Self- or AI-assessed sprint quality

Auto-generate summaries in `SPRINT_METRICS.md`.

---

## 🧩 Optional Extensions

- **GitHub Integration:** Auto-tag commits per agent.
- **Linear / Notion Sync:** Backlog and sprint API sync.
- **Retros Bot:** Analyze commits & logs to propose improvements.
- **Chat Interface:** Voice/chat access for daily stand-ups.

---

## ✅ How to Use in Cursor
1. Create the folder structure above.
2. Add agent prompt markdown files under `/.agents/`.
3. Use Cursor's multi-agent chat to assign roles and run sprints.
4. Maintain logs in `/sprints/` and `/docs/`.
5. Periodically prompt the Scrum Master to generate retros.

---

## 🧭 Next Steps
- [ ] Initialize project with `/backlog/BACKLOG.md`.
- [ ] Define first `EPIC` and its user stories.
- [ ] Run `SPRINT_01` simulation end-to-end.
- [ ] Add automation layer (Zapier, Notion, or GitHub).

