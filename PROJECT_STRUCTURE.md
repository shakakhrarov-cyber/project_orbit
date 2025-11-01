# 📁 ORBIT Project Structure

Complete file structure for the Agile Scrum Framework with AI Agents.

---

## Directory Tree

```
ORBIT/
│
├── 📄 README.md                    # Main framework documentation
├── 📄 QUICKSTART.md                # Quick start guide
├── 📄 PROJECT_STRUCTURE.md         # This file - structure overview
├── 📄 .gitignore                   # Git ignore rules
├── 📄 .cursorignore                # Cursor ignore rules
│
├── 📁 .agents/                     # AI Agent Role Definitions
│   ├── product_owner.prompt.md    # Product Owner agent instructions
│   ├── scrum_master.prompt.md     # Scrum Master agent instructions
│   ├── developer.prompt.md        # Developer agent instructions
│   ├── qa.prompt.md                # QA Engineer agent instructions
│   └── architect.prompt.md         # Software Architect agent instructions
│
├── 📁 docs/                        # Core Documentation
│   ├── ROADMAP.md                  # Product vision and quarterly goals
│   ├── ARCH_NOTES.md               # Architecture decisions and notes
│   └── TEST_PLAN.md                # Testing strategy and test cases
│
├── 📁 backlog/                     # Product Backlog Management
│   ├── BACKLOG.md                  # Prioritized product backlog
│   ├── EPICS.md                    # High-level epics
│   └── USER_STORIES.md             # Detailed user stories
│
└── 📁 sprints/                     # Sprint Execution
    ├── SPRINT_METRICS.md           # Cross-sprint metrics dashboard
    └── SPRINT_01/                  # Example sprint folder
        ├── SPRINT_PLAN.md          # Sprint planning document
        ├── DAILY_LOG.md            # Daily stand-up logs
        ├── SPRINT_REVIEW.md        # Sprint review summary
        └── RETRO.md                # Sprint retrospective
```

---

## 📂 Directory Descriptions

### `.agents/` - AI Agent Roles
Contains prompt definitions for each AI agent role. These files define:
- Role responsibilities
- Process guidelines
- Output formats
- Best practices

**Agents:**
- **Product Owner**: Manages product backlog and vision
- **Scrum Master**: Facilitates process and removes blockers
- **Developer**: Implements features and writes code
- **QA Engineer**: Tests and ensures quality
- **Architect**: Maintains architectural consistency

---

### `docs/` - Core Documentation
Strategic and technical documentation:

- **ROADMAP.md**: Product vision, quarterly goals, OKRs
- **ARCH_NOTES.md**: Architecture decisions (ADRs), tech stack, patterns
- **TEST_PLAN.md**: Testing strategy, test cases, quality gates

---

### `backlog/` - Product Backlog
Product backlog management files:

- **BACKLOG.md**: Prioritized list of all work items
- **EPICS.md**: High-level feature epics spanning multiple sprints
- **USER_STORIES.md**: Detailed user stories with acceptance criteria

---

### `sprints/` - Sprint Execution
Sprint-by-sprint execution tracking:

- **SPRINT_METRICS.md**: Aggregate metrics across all sprints
- **SPRINT_XX/**: Individual sprint folders containing:
  - **SPRINT_PLAN.md**: Sprint goal, committed stories, tasks
  - **DAILY_LOG.md**: Daily stand-up updates
  - **SPRINT_REVIEW.md**: Completed work and stakeholder feedback
  - **RETRO.md**: Retrospective insights and action items

---

## 🔄 File Relationships

```
ROADMAP.md
    ↓
EPICS.md
    ↓
USER_STORIES.md
    ↓
BACKLOG.md
    ↓
SPRINT_PLAN.md
    ↓
DAILY_LOG.md
    ↓
SPRINT_REVIEW.md + RETRO.md
    ↓
SPRINT_METRICS.md
```

---

## 📝 File Usage by Role

### Product Owner
- ✏️ ROADMAP.md
- ✏️ EPICS.md
- ✏️ USER_STORIES.md
- ✏️ BACKLOG.md
- 📖 SPRINT_REVIEW.md

### Scrum Master
- ✏️ SPRINT_PLAN.md
- ✏️ DAILY_LOG.md
- ✏️ SPRINT_REVIEW.md
- ✏️ RETRO.md
- ✏️ SPRINT_METRICS.md
- 📖 BACKLOG.md

### Developer
- 📖 SPRINT_PLAN.md
- 📖 ARCH_NOTES.md
- 📖 USER_STORIES.md
- ✏️ DAILY_LOG.md (updates)

### QA Engineer
- 📖 TEST_PLAN.md
- 📖 SPRINT_PLAN.md
- ✏️ TEST_PLAN.md (test cases)
- 📖 USER_STORIES.md

### Architect
- ✏️ ARCH_NOTES.md
- 📖 ROADMAP.md
- 📖 EPICS.md
- 📖 SPRINT_PLAN.md

**Legend**: ✏️ Primary editor | 📖 Reader/Consumer

---

## 🎯 Getting Started

1. **Start here**: `README.md` - Understand the framework
2. **Quick setup**: `QUICKSTART.md` - Step-by-step guide
3. **Define vision**: `docs/ROADMAP.md` - Set your goals
4. **Create epics**: `backlog/EPICS.md` - Break down vision
5. **Plan sprint**: `sprints/SPRINT_01/SPRINT_PLAN.md` - Begin execution

---

## 📊 Key Metrics Files

Track progress through these files:
- `SPRINT_METRICS.md` - Velocity, quality, team health
- `SPRINT_REVIEW.md` - Sprint completion data
- `RETRO.md` - Improvement tracking
- `BACKLOG.md` - Backlog health statistics

---

## 🔧 Configuration Files

- `.gitignore` - Excludes build artifacts, dependencies, temp files
- `.cursorignore` - Cursor-specific ignore patterns

---

## 🚀 Next Sprint Setup

To start a new sprint, copy the SPRINT_01 template:

```bash
cp -r sprints/SPRINT_01 sprints/SPRINT_02
```

Then update the sprint number in all files.

---

## 📚 Documentation Standards

All markdown files follow:
- Clear headings and sections
- Consistent formatting
- Template placeholders marked with `[brackets]`
- Date format: `YYYY-MM-DD`
- Regular updates with "Last Updated" timestamps

---

## 🤝 Contributing

When adding new files:
1. Follow the existing structure
2. Use clear, descriptive names
3. Include documentation headers
4. Update this structure file
5. Add to appropriate `.ignore` files if needed

---

*This structure supports scalable, AI-assisted Agile development in Cursor.*

