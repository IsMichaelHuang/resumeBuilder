# Resume Versions - Modular Structure

## Directory Structure

```
/resume/
├── preamble.tex           # Shared LaTeX formatting & packages
├── sections/              # Shared sections across all versions
│   ├── heading.tex        # Name, contact info
│   ├── education.tex      # Cal Poly education
│   ├── experience.tex     # Professional experience (shared)
│   └── hackathon.tex      # Merged hackathon wins
└── versions/              # Tailored resume versions
    ├── ai-ml/
    │   ├── main.tex       # Compile this file
    │   ├── summary.tex    # AI/ML-focused summary
    │   ├── projects.tex   # GAN, CNN
    │   └── skills.tex     # AI/ML skills emphasized
    ├── fullstack/
    │   ├── main.tex
    │   ├── summary.tex    # Full-stack-focused summary
    │   ├── projects.tex   # MERN Dashboard, Linux Shell
    │   └── skills.tex     # Frontend/Backend emphasized
    ├── backend/
    │   ├── main.tex
    │   ├── summary.tex    # Backend-focused summary
    │   ├── projects.tex   # Linux Shell, Huffman
    │   └── skills.tex     # Systems/APIs emphasized
    └── general-swe/
        ├── main.tex
        ├── summary.tex    # General SWE summary
        ├── projects.tex   # Balanced mix
        └── skills.tex     # Balanced skills
```

## Which Version to Use?

| Job Posting Keywords | Use This Version |
|---------------------|------------------|
| AI, ML, LLM, PyTorch, Deep Learning | `ai-ml/` |
| React, Node, Full-Stack, MERN, Frontend | `fullstack/` |
| Backend, APIs, Systems, Infrastructure | `backend/` |
| General SWE, New Grad Program | `general-swe/` |

## How to Compile

```bash
# Navigate to the specific version
cd versions/ai-ml

# Compile the resume
pdflatex main.tex
```

## How to Edit

### To update shared content (heading, education, experience, hackathon):
Edit files in `sections/`

### To update version-specific content:
1. **Summary**: Edit `summary.tex` in the specific version folder
2. **Projects**: Edit `projects.tex` in the specific version folder
3. **Skills**: Edit `skills.tex` in the specific version folder

### To add a new version:
1. Create new folder: `mkdir versions/new-version`
2. Copy template: `cp versions/general-swe/* versions/new-version/`
3. Customize the new files (especially `summary.tex` for the target role)

## Pro Tips

1. **Keyword matching**: Before applying, copy job description keywords into the appropriate `skills.tex`
2. **One page rule**: Each version should stay 1 page. Swap projects, don't add more.
3. **Test compile**: Always compile and check PDF before applying
4. **Name your PDFs**: Save as `Michael_Huang_Resume_AI_ML.pdf` (not just `resume.pdf`)
