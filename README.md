# Michael Huang - Resume System

A modular LaTeX resume system with a Python build pipeline. Assembles tailored 1-page resumes from shared sections and version-specific content, plus a multi-page monster (master) resume.

---

## Directory Structure

```
resume/
├── build                        # Python build script (assembles + compiles)
├── .env                         # Personal info (gitignored)
├── .env.example                 # Template for .env
├── .gitignore
├── output/                      # Compiled PDFs land here (gitignored)
├── tests/
│   └── test_build.py            # Test suite (pytest)
├── monster/                     # Self-contained master resume (all content)
│   └── main.tex
└── src/                         # All LaTeX source material
    ├── preamble.tex             # Shared packages & custom commands
    ├── sections/
    │   ├── heading.tex          # Name, contact info, links
    │   ├── education.tex        # Degrees and coursework
    │   ├── experience.tex       # Professional experience entries
    │   ├── skills.tex           # Technical skills (shared across all versions)
    │   └── projects/
    │       ├── axion.tex        # Axion Prompt Learning Module
    │       ├── sar.tex          # SAR Multi-Agent Deployment Pipeline
    │       ├── finance_dashboard.tex
    │       └── linux_shell.tex
    └── versions/
        ├── ai-ml/
        │   └── summary.tex      # AI/ML-tailored summary blurb
        └── fullstack/
            └── summary.tex      # Full-stack-tailored summary blurb
```

---

## How It Works

1. **Shared sections** live in `src/sections/` and are used by all versions.
2. **Version-specific content** is just the summary blurb in each version directory.
3. **Project snippets** in `src/sections/projects/` are cherry-picked per version via the `VERSIONS` config in `build`.
4. **`SECTION_ORDER`** in `build` controls the order of sections in the final document. Reorder or comment out entries to change what appears.
5. At build time, the script assembles a single `main.tex`, compiles it with `pdflatex`, moves the PDF to `output/`, and cleans up artifacts.

---

## Quick Start

### Prerequisites
- **Python 3.10+**
- **pdflatex** (via [MacTeX](https://www.tug.org/mactex/): `brew install --cask mactex`)
- **pytest** (for tests): `pip3 install pytest`

### Setup

```bash
cp .env.example .env
# Edit .env with your personal info (name, email, phone, etc.)
```

### Build

```bash
# Build a specific version
python3 build ai-ml
python3 build fullstack

# Build all tailored versions
python3 build all

# Build the monster (master) resume
python3 build monster
```

Output lands in `output/` as `Michael_Huang_Resume_<Label>.pdf`.

### Choose the Right Version

| Job Posting Mentions... | Use This Version |
|------------------------|------------------|
| AI, ML, LLM, PyTorch, Deep Learning | `ai-ml` |
| React, Node, Full-Stack, MERN | `fullstack` |

---

## How to Edit

### Shared Content (affects all versions)

| What | File |
|------|------|
| Contact info | `src/sections/heading.tex` |
| Education | `src/sections/education.tex` |
| Experience | `src/sections/experience.tex` |
| Skills | `src/sections/skills.tex` |
| Formatting | `src/preamble.tex` |

### Adding a Project

1. Create a snippet in `src/sections/projects/` (e.g. `new_project.tex`)
2. Add the snippet name to the relevant version's `projects` list in `build`
3. Run `python3 build all`

### Editing a Summary

Edit `src/versions/<version>/summary.tex`, then `python3 build <version>`.

### Changing Section Order

Edit the `SECTION_ORDER` list in `build`. Move, add, or comment out entries.

---

## Monster Resume

The monster resume at `monster/` is a multi-page master document containing all experience, projects, and skills. It has its own self-contained `main.tex` and skips the assembly pipeline.

**Workflow:** Update the monster first when adding new experience, then create snippets in `src/sections/` for the tailored versions.

---

## Testing

```bash
python3 -m pytest tests/ -v
```

33 tests covering env loading, template injection, snippet reading, project assembly, document assembly, config integrity, and heading placeholders.

---

## Troubleshooting

### "pdflatex: command not found"
```bash
export PATH="/Library/TeX/texbin:$PATH"
```

### Resume exceeds one page
1. Remove a project or bullet point
2. Adjust spacing in `src/preamble.tex`
3. Don't reduce font size below 11pt (ATS compatibility)
