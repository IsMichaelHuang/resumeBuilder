# Monster Resume - Master Document

## What is This?

Your **Monster Resume** is your **master repository** of ALL your experiences, projects, and skills. It's intentionally **multi-page** (that's OK!) and serves as your single source of truth.

Think of it as your **personal library** - you keep everything here, then **copy-paste** relevant sections into your tailored 1-page resumes.

---

## Contents

This monster resume includes:

- **ALL experiences** (current + templates for teaching, research, etc.)
- **ALL projects** (AI/ML, Full-Stack, Systems - every project you've done)
- **ALL skills** (comprehensive list across all domains)
- **Templates** for adding new content
- **Comments** explaining what to include

---

## How to Use It

### 1. Maintain It - Keep Everything Updated Here

When you:
- Complete a new project -- add it to `monster/projects.tex`
- Learn a new technology -- add it to `monster/skills.tex`
- Get a new job/internship -- add it to `monster/experience.tex`

**This is your single source of truth.** Update here FIRST, then copy to tailored versions.

### 2. Copy From It - Grab Sections for Tailored Resumes

When creating/updating a tailored resume:

```bash
# 1. Open the monster resume
code monster/projects.tex

# 2. Find the project you want
# 3. Copy the entire \resumeProjectHeading{...} block

# 4. Open the tailored version
code versions/ai-ml/projects.tex

# 5. Paste it in
# 6. Recompile
cd versions/ai-ml && pdflatex main.tex
```

### 3. Reference It - See All Your Options

Before applying to a job:
1. Open `monster/` files
2. See ALL your projects/experiences
3. Choose the most relevant ones
4. Copy to the appropriate tailored version

---

## Compiling the Monster Resume

```bash
cd monster
pdflatex main.tex
open main.pdf
```

**Note:** This will be **multiple pages** - that's expected and OK! This is NOT for job applications; it's your master document.

---

## Adding New Content

### Adding a New Experience

Edit `monster/experience.tex`:

```latex
\resumeSubheading
  {Company Name}{Start Date -- End Date}
  {Your Title}{Location}
  \resumeItemListStart
    \resumeItem{Achievement with quantified impact (X% improvement, $Y saved, Z users)}
    \resumeItem{Technical challenge and how you solved it}
    \resumeItem{Technologies used and scale (e.g., "handled 10K requests/sec")}
  \resumeItemListEnd
```

**Tips:**
- Use action verbs: Built, Architected, Implemented, Optimized, Designed
- Quantify everything: numbers, percentages, metrics
- Include impact: what changed because of your work?

### Adding a New Project

Edit `monster/projects.tex`:

```latex
\resumeProjectHeading{\textbf{Project Name} $|$ \emph{Tech Stack}}{}
    \resumeItemListStart
        \resumeItem{What you built and why}
        \resumeItem{Technical details or challenges}
        \resumeItem{(Optional) Impact or outcome}
    \resumeItemListEnd
```

### Adding New Skills

Edit `monster/skills.tex`:

Just add to the appropriate category. For example:
```latex
\textbf{AI/ML: }{PyTorch, TensorFlow, NEW_SKILL, Gemini API, ...}
```

---

## Monster vs Tailored Versions

| Monster Resume | Tailored Versions |
|----------------|-------------------|
| **Multi-page** (2-4 pages) | **1 page only** |
| ALL experiences | Most relevant 2-3 experiences |
| ALL projects (6-8+) | Most relevant 2-3 projects |
| ALL skills | Skills relevant to role |
| **Purpose:** Archive & source | **Purpose:** Job applications |
| **Audience:** You | **Audience:** Recruiters |
| Update when learning | Copy from monster when applying |

---

## File Structure

```
monster/
├── README.md           # This file
├── main.tex            # Compiles the full monster resume
├── experience.tex      # ALL experiences (with templates)
├── projects.tex        # ALL projects (organized by category)
└── skills.tex          # ALL skills (comprehensive)
```

---

## Important Notes

1. **Never send the monster resume to employers** - It's multi-page and too comprehensive
2. **Always copy FROM monster TO tailored versions** - Never the reverse
3. **Update monster first** - It's your source of truth
4. **Don't worry about page limits here** - That's for tailored versions only
5. **Keep templates** - The commented templates help maintain consistency
