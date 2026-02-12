# Michael Huang - Resume System

A modular, DRY (Don't Repeat Yourself) LaTeX resume system with a **Monster Resume** (master document) and 4 tailored 1-page versions for different job types.

---

## Directory Structure

```
/resume/
├── README.md                     # This file
├── build.sh                      # Build script to compile resume PDFs
├── .gitignore                    # Ignore build artifacts
├── preamble.tex                  # Shared LaTeX packages & formatting
│
├── sections/                     # Shared content across all versions
│   ├── heading.tex              # Name & contact info
│   ├── education.tex            # Cal Poly SLO education
│   ├── experience.tex           # Professional experience (shared)
│   └── hackathon.tex            # Merged hackathon wins
│
├── monster/                      # MONSTER RESUME - Your Master Document
│   ├── README.md                # How to use the monster resume
│   ├── main.tex                 # Compiles full multi-page resume
│   ├── experience.tex           # ALL experiences (with templates)
│   ├── projects.tex             # ALL projects (organized by type)
│   └── skills.tex               # ALL skills (comprehensive)
│
└── versions/                     # 4 tailored 1-page resume versions
    ├── README.md                # Version-specific documentation
    │
    ├── ai-ml/                   # AI/ML Engineer version (1 page)
    │   ├── main.tex             # Compile this file
    │   ├── summary.tex          # AI/ML-focused summary
    │   ├── projects.tex         # GAN, CNN
    │   └── skills.tex           # AI/ML skills emphasized
    │
    ├── fullstack/               # Full-Stack Engineer version (1 page)
    │   ├── main.tex
    │   ├── summary.tex          # Full-stack-focused summary
    │   ├── projects.tex         # MERN Dashboard, Linux Shell
    │   └── skills.tex           # Frontend/Backend emphasized
    │
    ├── backend/                 # Backend/Infrastructure version (1 page)
    │   ├── main.tex
    │   ├── summary.tex          # Backend-focused summary
    │   ├── projects.tex         # Linux Shell, Huffman
    │   └── skills.tex           # Systems/APIs emphasized
    │
    └── general-swe/             # General SWE / New Grad version (1 page)
        ├── main.tex
        ├── summary.tex          # General SWE summary
        ├── projects.tex         # Balanced project mix
        └── skills.tex           # Balanced skills
```

---

## Monster Resume - Your Master Document

The **Monster Resume** at `monster/` contains ALL your experiences, projects, and skills. This is your **single source of truth**.

**Workflow:**
1. **Update monster first** - When you complete projects, learn skills, get new jobs, add to `monster/`
2. **Copy to tailored versions** - When applying to jobs, copy relevant sections from `monster/` to `versions/[type]/`
3. **Keep tailored to 1 page** - `versions/` are for applications (1 page only)
4. **Monster can be multi-page** - That's OK! It's your personal archive

See [monster/README.md](monster/README.md) for details.

---

## Quick Start

### 1. Choose the Right Resume Version

| Job Posting Mentions... | Use This Version |
|------------------------|------------------|
| AI, ML, LLM, PyTorch, Deep Learning, Neural Networks | `ai-ml/` |
| React, Node, Full-Stack, MERN, Frontend, Backend | `fullstack/` |
| Backend, APIs, Systems, Infrastructure, Linux, Microservices | `backend/` |
| General Software Engineer, New Grad, SWE | `general-swe/` |

### 2. Compile the Resume

```bash
# Build a specific version
./build.sh ai-ml
./build.sh fullstack
./build.sh backend
./build.sh general-swe

# Build all 4 tailored versions at once
./build.sh all

# Build the monster (master) resume
./build.sh monster
```

**Output:** `main.pdf` in the version's directory (e.g. `versions/ai-ml/main.pdf`)

### 3. Rename for Application

```bash
# Copy to ~/Desktop with a descriptive name (default destination)
./build.sh rename ai-ml

# Copy to a custom directory
./build.sh rename ai-ml ./applications/

# Rename all 4 versions at once
./build.sh rename all
./build.sh rename all ./applications/
```

Output filenames follow the pattern `Michael_Huang_Resume_[Version].pdf`.

---

## How to Edit

### Editing Shared Content

These files are used by **ALL versions**. Edit once, affects all:

- **Contact Info**: Edit `sections/heading.tex`
- **Education**: Edit `sections/education.tex`
- **Experience**: Edit `sections/experience.tex`
- **Hackathon**: Edit `sections/hackathon.tex`
- **Formatting**: Edit `preamble.tex`

After editing shared files, recompile all versions:
```bash
./build.sh all
```

### Editing Version-Specific Content

These files are unique per version:

- **Summary**: Edit `versions/[version]/summary.tex`
- **Projects**: Edit `versions/[version]/projects.tex`
- **Skills**: Edit `versions/[version]/skills.tex`

After editing:
```bash
./build.sh [version]
```

---

## Key Differences Between Versions

### AI/ML Version
- **Summary**: Multi-agent orchestration, LLM integration, deep learning
- **Projects**: GAN, CNN
- **Skills Order**: AI/ML listed first
- **Best For**: ML Engineer, AI Engineer, Research roles

### Full-Stack Version
- **Summary**: MERN stack, AI-powered backends, microservices
- **Projects**: MERN Dashboard, Linux Shell
- **Skills Order**: Frontend/Backend split
- **Best For**: Full-Stack, Web Developer, Frontend/Backend roles

### Backend Version
- **Summary**: API design, systems programming, async architecture
- **Projects**: Linux Shell, Huffman Encoding
- **Skills Order**: Backend & Systems first
- **Best For**: Backend Engineer, Infrastructure, Systems roles

### General SWE Version
- **Summary**: Breadth across AI/ML, full-stack, and systems
- **Projects**: Balanced mix
- **Skills Order**: Balanced across all areas
- **Best For**: New Grad programs, General SWE positions

---

## Technical Details

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
\input{../../preamble}            % Goes up 2 levels to /resume/preamble.tex
\input{summary}                   % Loads summary.tex from same directory
\input{../../sections/heading}    % Goes up 2 levels to /resume/sections/heading.tex
\input{../../sections/experience} % Shared experience across all versions
\input{projects}                  % Loads projects.tex from same directory
```

This is why the structure is **DRY** - shared files are only stored once.

---

## Troubleshooting

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

## Changelog

- **2026-02-08**: Removed QUICK_REFERENCE.md and APPLICATION_TRACKER.md, added build.sh, recompiled all resume PDFs
- **2026-02-07**: Added tailored summary sections per version, merged hackathon entries, removed GPA
- **2026-02-01**: Initial modular system created with 4 versions
