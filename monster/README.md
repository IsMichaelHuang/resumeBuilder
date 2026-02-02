# Monster Resume - Master Document

## 🐉 What is This?

Your **Monster Resume** is your **master repository** of ALL your experiences, projects, and skills. It's intentionally **multi-page** (that's OK!) and serves as your single source of truth.

Think of it as your **personal library** - you keep everything here, then **copy-paste** relevant sections into your tailored 1-page resumes.

---

## 📋 Contents

This monster resume includes:

- ✅ **ALL experiences** (current + templates for teaching, research, etc.)
- ✅ **ALL projects** (AI/ML, Full-Stack, Systems - every project you've done)
- ✅ **ALL skills** (comprehensive list across all domains)
- ✅ **Templates** for adding new content
- ✅ **Comments** explaining what to include

---

## 🎯 How to Use It

### 1. **Maintain It** - Keep Everything Updated Here

When you:
- Complete a new project → Add it to `monster/projects.tex`
- Learn a new technology → Add it to `monster/skills.tex`
- Get a new job/internship → Add it to `monster/experience.tex`
- Teach a class → Add it to `monster/experience.tex`

**This is your single source of truth.** Update here FIRST, then copy to tailored versions.

### 2. **Copy From It** - Grab Sections for Tailored Resumes

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

### 3. **Reference It** - See All Your Options

Before applying to a job:
1. Open `monster/` files
2. See ALL your projects/experiences
3. Choose the most relevant ones
4. Copy to the appropriate tailored version

---

## 📄 Compiling the Monster Resume

```bash
cd monster
pdflatex main.tex
open main.pdf
```

**Note:** This will be **multiple pages** - that's expected and OK! This is NOT for job applications; it's your master document.

---

## ✂️ Copy-Paste Workflow

### Example: Adding a Project to AI/ML Resume

**Step 1:** Open monster projects
```bash
code monster/projects.tex
```

**Step 2:** Find the project (e.g., CNN project)
```latex
\resumeProjectHeading
    {\textbf{Convolutional Neural Network (CNN)} $|$ \emph{Python, PyTorch, Sklearn, Jupyter Notebook}}{}
      \resumeItemListStart
        \resumeItem{Built a CNN to classify images from a complex dataset. Incorporated data augmentation techniques like rotation, flipping, and zooming to improve generalization and reduce overfitting}
        \resumeItem{Used pretrained models like VGG19 to extract style and content features and applied optimization techniques to generate blended images. Experimented with different styles and evaluated the quality of the generated images}
\resumeItemListEnd
```

**Step 3:** Copy entire block (from `\resumeProjectHeading` to `\resumeItemListEnd`)

**Step 4:** Open tailored version
```bash
code versions/ai-ml/projects.tex
```

**Step 5:** Paste in the appropriate location

**Step 6:** Recompile
```bash
cd versions/ai-ml
pdflatex main.tex
```

---

## 🏗️ Adding New Content

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
        \resumeItem{What you built and why (e.g., "Built a web app to help students...")}
        \resumeItem{Technical details or challenges (e.g., "Implemented real-time sync using WebSockets")}
        \resumeItem{(Optional) Impact or outcome (e.g., "Used by 500+ students")}
    \resumeItemListEnd
```

### Adding New Skills

Edit `monster/skills.tex`:

Just add to the appropriate category. For example:
```latex
\textbf{AI/ML: }{PyTorch, TensorFlow, NEW_SKILL, Gemini API, ...}
```

---

## 🎨 Monster vs Tailored Versions

| Monster Resume | Tailored Versions |
|----------------|-------------------|
| **Multi-page** (2-4 pages) | **1 page only** |
| ALL experiences | Most relevant 2-3 experiences |
| ALL projects (6-8+) | Most relevant 3 projects |
| ALL skills | Skills relevant to role |
| **Purpose:** Archive & source | **Purpose:** Job applications |
| **Audience:** You | **Audience:** Recruiters |
| Update when learning | Copy from monster when applying |

---

## 📂 File Structure

```
monster/
├── README.md           # This file
├── main.tex            # Compiles the full monster resume
├── experience.tex      # ALL experiences (with templates)
├── projects.tex        # ALL projects (organized by category)
└── skills.tex          # ALL skills (comprehensive)
```

---

## 💡 Pro Tips

### 1. Update Regularly
Don't wait until job hunting. Add things as you do them:
- Finished a project? → Add to monster immediately
- Learned a new framework? → Add to skills
- Got a new responsibility at work? → Update experience

### 2. Be Specific
Monster resume can have more detail than tailored versions:
- Include ALL technologies used
- Mention ALL techniques/algorithms
- Add context that you'll trim for 1-page versions

### 3. Use Categories
Organize projects by type (AI/ML, Web Dev, Systems) so you can find them easily when tailoring.

### 4. Keep Templates
The template comments in the files are there to help you add new content consistently.

### 5. Version Control
Consider using git for the monster resume:
```bash
git add monster/
git commit -m "Added new project: XYZ"
```

---

## 🔄 Workflow Summary

```
New Skill/Project/Experience
        ↓
Add to monster/ first (single source of truth)
        ↓
Job opportunity appears
        ↓
Analyze job description
        ↓
Open monster/ and find relevant content
        ↓
Copy to appropriate versions/[type]/
        ↓
Ensure 1-page limit (remove less relevant items)
        ↓
Recompile & apply
```

---

## ⚠️ Important Notes

1. **Never send the monster resume to employers** - It's multi-page and too comprehensive
2. **Always copy FROM monster TO tailored versions** - Never the reverse
3. **Update monster first** - It's your source of truth
4. **Don't worry about page limits here** - That's for tailored versions only
5. **Keep templates** - The commented templates help maintain consistency

---

## 🎯 Quick Commands

```bash
# Compile monster resume
cd monster && pdflatex main.tex

# Edit monster files
code monster/experience.tex
code monster/projects.tex
code monster/skills.tex

# Copy to tailored version (example)
# 1. Copy from monster/projects.tex
# 2. Paste into versions/ai-ml/projects.tex
# 3. Recompile: cd versions/ai-ml && pdflatex main.tex
```

---

## 📊 What to Track

Keep in the monster resume but maybe cut from tailored:
- Older projects (2+ years ago)
- Course projects (unless very impressive)
- Extra responsibilities you've had
- Technologies you know but aren't currently focusing on
- Complete list of everything you've built

---

**Remember: The monster resume is YOUR document. Make it as detailed and comprehensive as you want. Tailored versions are for recruiters - keep those to 1 page.**
