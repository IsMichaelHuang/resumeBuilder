# Michael Huang - Resume System

A modular, DRY (Don't Repeat Yourself) LaTeX resume system with a **Monster Resume** (master document) and 4 tailored 1-page versions for different job types.

---

## 📁 Directory Structure

```
/resume/
├── README.md                     # This file - main documentation
├── QUICK_REFERENCE.md            # Cheat sheet for quick lookup
├── APPLICATION_TRACKER.md        # Track your job applications
├── .gitignore                    # Ignore build artifacts
├── preamble.tex                  # Shared LaTeX packages & formatting
│
├── sections/                     # Shared content across all versions
│   ├── heading.tex              # Your name & contact info
│   ├── education.tex            # Cal Poly SLO education
│   └── hackathon.tex            # SkepticScript hackathon win
│
├── monster/                      # 🐉 MONSTER RESUME - Your Master Document
│   ├── README.md                # How to use the monster resume
│   ├── main.tex                 # Compiles full multi-page resume
│   ├── experience.tex           # ALL experiences (with templates)
│   ├── projects.tex             # ALL projects (organized by type)
│   └── skills.tex               # ALL skills (comprehensive)
│
├── versions/                     # 4 tailored 1-page resume versions
│   ├── README.md                # Version-specific documentation
│   │
│   ├── ai-ml/                   # AI/ML Engineer version (1 page)
│   │   ├── main.tex             # Compile this file → PDF
│   │   ├── experience.tex       # AI-focused experience
│   │   ├── projects.tex         # GAN, CNN, Neural Networks
│   │   └── skills.tex           # AI/ML skills emphasized
│   │
│   ├── fullstack/               # Full-Stack Engineer version (1 page)
│   │   ├── main.tex
│   │   ├── experience.tex
│   │   ├── projects.tex         # MERN, Linux Shell, GAN
│   │   └── skills.tex           # Frontend/Backend emphasized
│   │
│   ├── backend/                 # Backend/Infrastructure version (1 page)
│   │   ├── main.tex
│   │   ├── experience.tex
│   │   ├── projects.tex         # Linux Shell, Huffman, MERN
│   │   └── skills.tex           # Systems/APIs emphasized
│   │
│   └── general-swe/             # General SWE / New Grad version (1 page)
│       ├── main.tex
│       ├── experience.tex
│       ├── projects.tex         # Balanced project mix
│       └── skills.tex           # Balanced skills
│
└── coverLetter/
    └── Hex_Cover_Letter.tex     # Cover letter template
```

---

## 🐉 Monster Resume - Your Master Document

**NEW:** You now have a **Monster Resume** at `monster/` that contains ALL your experiences, projects, and skills. This is your **single source of truth**.

**Workflow:**
1. **Update monster first** - When you complete projects, learn skills, get new jobs → add to `monster/`
2. **Copy to tailored versions** - When applying to jobs → copy relevant sections from `monster/` to `versions/[type]/`
3. **Keep tailored to 1 page** - `versions/` are for applications (1 page only)
4. **Monster can be multi-page** - That's OK! It's your personal archive

See [monster/README.md](monster/README.md) for details.

---

## 🚀 Quick Start

### 1. Choose the Right Resume Version

| Job Posting Mentions... | Use This Version |
|------------------------|------------------|
| AI, ML, LLM, PyTorch, Deep Learning, Neural Networks | `ai-ml/` |
| React, Node, Full-Stack, MERN, Frontend, Backend | `fullstack/` |
| Backend, APIs, Systems, Infrastructure, Linux, Microservices | `backend/` |
| General Software Engineer, New Grad, SWE | `general-swe/` |

### 2. Compile the Resume

```bash
# Navigate to the version you want
cd versions/ai-ml

# Compile to PDF
pdflatex main.tex

# Open the PDF
open main.pdf
```

**Output:** `main.pdf` in the same directory

### 3. Rename for Application

```bash
# Copy with descriptive name
cp main.pdf ~/Desktop/Michael_Huang_Resume_AI_ML.pdf
```

---

## ✏️ How to Edit

### Editing Shared Content

These files are used by **ALL versions**. Edit once, affects all:

- **Contact Info**: Edit `sections/heading.tex`
- **Education**: Edit `sections/education.tex`
- **Hackathon**: Edit `sections/hackathon.tex`
- **Formatting**: Edit `preamble.tex`

After editing shared files:
```bash
# Recompile all versions
cd versions/ai-ml && pdflatex main.tex
cd versions/fullstack && pdflatex main.tex
cd versions/backend && pdflatex main.tex
cd versions/general-swe && pdflatex main.tex
```

### Editing Version-Specific Content

These files are unique per version:

- **Experience**: Edit `versions/[version]/experience.tex`
- **Projects**: Edit `versions/[version]/projects.tex`
- **Skills**: Edit `versions/[version]/skills.tex`

After editing:
```bash
cd versions/[version]
pdflatex main.tex
```

---

## 🎯 Customizing for a Specific Job

### Adding Job-Specific Keywords

1. **Read the job description** and identify key technologies
2. **Check if keywords are in your resume:**
   - Open `versions/[version]/skills.tex`
   - See if the keywords are listed
3. **If missing, add them:**
   ```bash
   # Open the skills file
   code versions/ai-ml/skills.tex

   # Add keywords (only if you actually have that skill!)
   # For example, add "TensorFlow" to AI/ML line

   # Recompile
   cd versions/ai-ml
   pdflatex main.tex
   ```

### Example: Adding "TensorFlow" to AI/ML Resume

Edit `versions/ai-ml/skills.tex`:
```latex
\textbf{AI/ML: }{PyTorch, Gemini API, TensorFlow, Azure Speech SDK, Sklearn, ...}
```

Recompile:
```bash
cd versions/ai-ml
pdflatex main.tex
```

---

## 📋 Application Workflow

### For Each Job Application:

1. **Analyze the job posting**
   - What are the top 5 technical requirements?
   - Which resume version matches best?

2. **Check keyword alignment**
   - Open the appropriate `skills.tex`
   - Add any missing keywords you actually possess

3. **Compile the resume**
   ```bash
   cd versions/[chosen-version]
   pdflatex main.tex
   ```

4. **Name it appropriately**
   ```bash
   cp main.pdf ~/Desktop/Michael_Huang_Resume_[Company]_[Role].pdf
   ```

5. **Apply**
   - ✅ Apply on **company website** (higher success rate)
   - ❌ Avoid only using LinkedIn Easy Apply

6. **Track it**
   - Open `APPLICATION_TRACKER.md`
   - Add company, date, status, follow-up date

7. **Follow up after 1 week** if no response

---

## 🎨 Key Differences Between Versions

### AI/ML Version
- **Projects**: GAN, CNN, Neural Network optimization
- **Skills Order**: AI/ML listed first
- **Keywords**: PyTorch, LLMs, Generative AI, Deep Learning
- **Best For**: ML Engineer, AI Engineer, Research roles

### Full-Stack Version
- **Projects**: MERN Dashboard, Linux Shell, GAN
- **Skills Order**: Frontend/Backend split
- **Keywords**: React, Node.js, Express, MongoDB, TypeScript
- **Best For**: Full-Stack, Web Developer, Frontend/Backend roles

### Backend Version
- **Projects**: Linux Shell, Huffman Encoding, MERN Dashboard
- **Skills Order**: Backend & Systems first
- **Keywords**: APIs, Microservices, Linux, POSIX, Systems Programming
- **Best For**: Backend Engineer, Infrastructure, Systems roles

### General SWE Version
- **Projects**: Balanced mix (MERN, GAN, Linux Shell)
- **Skills Order**: Balanced across all areas
- **Keywords**: Mix of all technical skills
- **Best For**: New Grad programs, General SWE positions

---

## 🛠️ Common Tasks

### Task: Add a New Experience

1. **Choose which versions need it** (AI/ML, Full-Stack, Backend, or all?)
2. **Edit the experience files:**
   ```bash
   code versions/ai-ml/experience.tex
   ```
3. **Add using the resume commands:**
   ```latex
   \resumeSubheading
     {Company Name} {Start Date -- End Date}
     {Your Title} {Location}
     \resumeItemListStart
       \resumeItem{Achievement with quantified impact}
       \resumeItem{Another achievement with metrics}
     \resumeItemListEnd
   ```
4. **Recompile:**
   ```bash
   cd versions/ai-ml && pdflatex main.tex
   ```

### Task: Add a New Project

1. **Decide which version(s) should showcase this project**
2. **Edit the projects file:**
   ```bash
   code versions/fullstack/projects.tex
   ```
3. **Add the project:**
   ```latex
   \resumeProjectHeading{\textbf{Project Name} $|$ \emph{Tech Stack}}{}
     \resumeItemListStart
       \resumeItem{What you built and the impact}
       \resumeItem{Technical challenges you solved}
     \resumeItemListEnd
   ```
4. **Recompile:**
   ```bash
   cd versions/fullstack && pdflatex main.tex
   ```

### Task: Update Contact Info

1. **Edit the shared heading:**
   ```bash
   code sections/heading.tex
   ```
2. **Make your changes**
3. **Recompile ALL versions** (since heading is shared):
   ```bash
   for version in ai-ml fullstack backend general-swe; do
     cd versions/$version && pdflatex main.tex && cd ../..
   done
   ```

### Task: Create a New Resume Version

1. **Copy an existing version:**
   ```bash
   cp -r versions/general-swe versions/teaching
   ```
2. **Edit the version-specific files:**
   - `experience.tex` - Add teaching experience
   - `projects.tex` - Add relevant projects
   - `skills.tex` - Emphasize relevant skills
3. **Update main.tex if needed** (usually no changes needed)
4. **Compile:**
   ```bash
   cd versions/teaching && pdflatex main.tex
   ```

---

## 📊 Tracking Your Applications

Use `APPLICATION_TRACKER.md` to:
- Track which companies you applied to
- Record which resume version you used
- Note application status and follow-up dates
- Calculate your response rate
- Identify what's working

**Goal: 20-30% response rate** (2-3 responses per 10 applications)

If your response rate is lower:
1. Are you tailoring keywords for each job?
2. Are you applying to appropriate roles for your experience level?
3. Are you applying directly on company websites?
4. Is your resume showing quantified impact?

---

## ⚙️ Technical Details

### Prerequisites
- **MacTeX** (installed via `brew install --cask mactex`)
- **pdflatex** command available in PATH

### Compiling from Command Line
```bash
# Single compilation
pdflatex main.tex

# Full compilation (3 passes for proper references)
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

### File Paths Explained
Each version's `main.tex` uses relative paths:
```latex
\input{../../preamble}          % Goes up 2 levels to /resume/preamble.tex
\input{../../sections/heading}  % Goes up 2 levels to /resume/sections/heading.tex
\input{experience}              % Loads experience.tex from same directory
```

This is why the structure is **DRY** - shared files are only stored once.

---

## 💡 Pro Tips

### Resume Tips
1. **One page only** - If adding content, remove something else
2. **Quantify everything** - Use numbers, percentages, metrics
3. **Action verbs** - Built, Architected, Implemented, Optimized
4. **Keywords matter** - Mirror the job description language
5. **No typos** - Always proofread before submitting

### Application Tips
1. **Apply early** - First 100 applicants have highest review rate
2. **Best times**: Monday-Wednesday, 6-10 AM PT
3. **Quality > Quantity** - 10 tailored apps > 50 generic ones
4. **Follow up** - Polite email after 1 week if no response
5. **Direct applications** - Company website > LinkedIn Easy Apply

### System Maintenance
1. **Keep versions in sync** - If you update shared files, recompile all
2. **Version control** - Consider using git to track changes
3. **Backup PDFs** - Save copies of successful applications
4. **Update regularly** - Add new skills/projects as you learn them

---

## 🐛 Troubleshooting

### "pdflatex: command not found"
```bash
# Add to PATH
export PATH="/Library/TeX/texbin:$PATH"

# Or restart your terminal
```

### "File not found: ../../preamble.tex"
- Make sure you're in the correct directory
- Should be in `versions/[version]/` when compiling
- Check that `preamble.tex` exists in the root `/resume/` directory

### "LaTeX Error: File '*.sty' not found"
- Missing LaTeX package
- Install with: `sudo tlmgr install [package-name]`
- Or use MacTeX which includes all packages

### Resume exceeds one page
1. Reduce margins (edit `preamble.tex`)
2. Remove a project or bullet point
3. Tighten vertical spacing
4. **Don't** reduce font size below 11pt (ATS may have issues)

### Changes not showing in PDF
- Make sure you saved the `.tex` file
- Recompile: `pdflatex main.tex`
- Sometimes need to delete auxiliary files: `rm *.aux *.log *.out`

---

## 📚 Resources

- **LaTeX Documentation**: [Overleaf Docs](https://www.overleaf.com/learn)
- **Resume Writing**: [Resume Worded](https://resumeworded.com/)
- **ATS Optimization**: [Jobscan](https://www.jobscan.co/)
- **Tech Interview Prep**: [LeetCode](https://leetcode.com/)

---

## 🎯 Next Steps

1. ✅ System is set up and all versions compile
2. [ ] Choose 5 companies to apply to this week
3. [ ] Match each to appropriate resume version
4. [ ] Customize keywords if needed
5. [ ] Apply and track in APPLICATION_TRACKER.md
6. [ ] Follow up after 1 week

**Target: 10-15 applications per week with 20-30% response rate**

---

## 📝 Changelog

- **2026-02-01**: Initial modular system created with 4 versions
- Future updates will be tracked here

---

## 📧 Questions?

If you need to modify the structure or add features:
1. Check `versions/README.md` for version-specific details
2. Reference this main README for overall system
3. Review LaTeX documentation for syntax questions

**Remember: Quality applications > Quantity. Take your time!**
