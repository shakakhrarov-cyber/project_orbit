# 🚀 Quick Start Guide

Get started with the Agile Scrum Framework for AI Agents in Cursor in just a few steps!

---

## 📋 Prerequisites

- **Cursor IDE** installed
- Basic understanding of Agile/Scrum methodology
- A project or product vision to implement

---

## 🎯 Step-by-Step Setup

### 1. Define Your Vision
Start by filling out the high-level project vision:

```bash
# Edit these files first:
docs/ROADMAP.md       # Define your product vision and quarterly goals
backlog/EPICS.md      # Break down vision into major epics
```

**Example**:
- **Vision**: Build a task management application
- **Epic 1**: User authentication system
- **Epic 2**: Task creation and management
- **Epic 3**: Team collaboration features

---

### 2. Create Your Product Backlog
Work with the **Product Owner Agent** to refine your backlog:

```
@ProductOwner, review the ROADMAP.md and create user stories for Epic 1 in USER_STORIES.md
```

The Product Owner will:
- Break epics into user stories
- Add acceptance criteria
- Estimate story points
- Prioritize by business value

---

### 3. Plan Your First Sprint
Use the **Scrum Master Agent** to plan Sprint 01:

```
@ScrumMaster, create a sprint plan for Sprint 01 using the top 5 prioritized items from BACKLOG.md
```

The Scrum Master will:
- Review team capacity
- Select stories for the sprint
- Break stories into tasks
- Create `sprints/SPRINT_01/SPRINT_PLAN.md`

---

### 4. Start Development
Activate the **Developer Agent** to begin implementation:

```
@Developer, implement US-001 from SPRINT_PLAN.md following the acceptance criteria
```

The Developer will:
- Write clean, documented code
- Create unit tests
- Follow architectural guidelines
- Commit with clear messages

---

### 5. Quality Assurance
Have the **QA Agent** validate the work:

```
@QA, review the implementation of US-001 and run all tests
```

The QA will:
- Execute test cases
- Verify acceptance criteria
- Check code quality
- Report any issues found

---

### 6. Architecture Review
Get the **Architect Agent** to review design decisions:

```
@Architect, review the implementation of US-001 for architectural consistency
```

The Architect will:
- Validate design patterns
- Check for technical debt
- Suggest improvements
- Update `ARCH_NOTES.md`

---

### 7. Daily Stand-ups
Each day, have the Scrum Master provide updates:

```
@ScrumMaster, generate today's stand-up summary from DAILY_LOG.md
```

The Scrum Master will report:
- Progress since last update
- Current blockers
- Next steps

---

### 8. Sprint Review
At sprint end, conduct a review:

```
@ScrumMaster, create the Sprint Review document showing completed work and gathering feedback
```

Demo completed features and gather stakeholder feedback.

---

### 9. Sprint Retrospective
Reflect on the sprint process:

```
@ScrumMaster, facilitate the Sprint 01 retrospective and identify improvement actions
```

Discuss:
- What went well
- What didn't go well
- Action items for next sprint

---

## 🎯 Example Workflow

### Complete Sprint Cycle Example

#### Day 1: Sprint Planning
```
You: @ScrumMaster, plan Sprint 01 with stories US-001, US-002, US-003
```

#### Days 2-9: Development & Daily Stand-ups
```
You: @Developer, implement US-001
[Development happens]

You: @QA, test US-001
[Testing happens]

You: @ScrumMaster, daily stand-up update
[Daily sync]
```

#### Day 10: Sprint Review & Retro
```
You: @ScrumMaster, conduct sprint review and retrospective
```

---

## 💡 Pro Tips

### 1. **Use Agent Tags Consistently**
Always address agents by their role:
- `@ProductOwner` - Backlog management
- `@ScrumMaster` - Process facilitation
- `@Developer` - Implementation
- `@QA` - Quality assurance
- `@Architect` - Design decisions

### 2. **Maintain Documentation**
Keep these files updated:
- `DAILY_LOG.md` - Daily progress
- `BACKLOG.md` - Current priorities
- `ARCH_NOTES.md` - Design decisions
- `TEST_PLAN.md` - Testing strategy

### 3. **Follow the Definition of Done**
Before marking stories complete:
- ✅ Code reviewed
- ✅ Tests passing
- ✅ Documentation updated
- ✅ Acceptance criteria met
- ✅ QA approved

### 4. **Track Metrics**
Regularly update `SPRINT_METRICS.md` to:
- Monitor velocity trends
- Identify bottlenecks
- Measure quality
- Track team health

### 5. **Keep Sprints Focused**
- Commit to realistic story points
- Minimize mid-sprint changes
- Address blockers quickly
- Stick to the sprint goal

---

## 🔄 Continuous Improvement

### After Each Sprint
1. **Review metrics** - Check velocity and quality trends
2. **Complete retro actions** - Implement improvement items
3. **Refine backlog** - Groom upcoming stories
4. **Update roadmap** - Adjust based on learnings

### Monthly
1. **Review roadmap progress** against quarterly goals
2. **Assess technical debt** and prioritize paydown
3. **Evaluate agent effectiveness** and refine prompts
4. **Update test plan** based on quality metrics

---

## 🆘 Troubleshooting

### Issue: Agent Not Following Instructions
**Solution**: Review and update agent prompt files in `.agents/` directory

### Issue: Stories Too Large
**Solution**: Have Product Owner break them down further (aim for 3-8 points)

### Issue: Low Velocity
**Solution**: Review retrospective for blockers and improvement actions

### Issue: Quality Issues
**Solution**: Strengthen Definition of Done and increase QA involvement

---

## 📚 Next Steps

1. ✅ Fill out `ROADMAP.md` with your vision
2. ✅ Create epics in `EPICS.md`
3. ✅ Generate user stories in `USER_STORIES.md`
4. ✅ Plan your first sprint
5. ✅ Start development!

---

## 🔗 Additional Resources

- **README.md** - Complete framework documentation
- **Agent Prompts** - `.agents/` directory
- **Sprint Templates** - `sprints/SPRINT_01/` directory
- **Metrics Dashboard** - `SPRINT_METRICS.md`

---

**Ready to get started? Begin with defining your vision in `docs/ROADMAP.md`!**

*Good luck with your AI-powered Agile development!* 🎉

