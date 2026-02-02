# Resume Versions - Modular Structure

## 📁 Directory Structure

```
/resume/
├── preamble.tex           # Shared LaTeX formatting & packages
├── main.tex              # Original master resume
├── sections/             # Shared sections across all versions
│   ├── heading.tex       # Name, contact info
│   ├── education.tex     # Cal Poly education
│   └── hackathon.tex     # SkepticScript hackathon win
└── versions/             # Tailored resume versions
    ├── ai-ml/
    │   ├── main.tex      # Compile this file
    │   ├── experience.tex    # AI-focused experience ordering
    │   ├── projects.tex      # GAN, CNN, Neural Network
    │   └── skills.tex        # AI/ML skills emphasized
    ├── fullstack/
    │   ├── main.tex
    │   ├── experience.tex
    │   ├── projects.tex      # MERN, Linux Shell, GAN
    │   └── skills.tex        # Frontend/Backend emphasized
    ├── backend/
    │   ├── main.tex
    │   ├── experience.tex
    │   ├── projects.tex      # Linux Shell, Huffman, MERN
    │   └── skills.tex        # Systems/APIs emphasized
    └── general-swe/
        ├── main.tex
        ├── experience.tex
        ├── projects.tex      # Balanced mix
        └── skills.tex        # Balanced skills
```

## 🎯 Which Version to Use?

| Job Posting Keywords | Use This Version |
|---------------------|------------------|
| AI, ML, LLM, PyTorch, Deep Learning | `ai-ml/` |
| React, Node, Full-Stack, MERN, Frontend | `fullstack/` |
| Backend, APIs, Systems, Infrastructure | `backend/` |
| General SWE, New Grad Program | `general-swe/` |

## 🔨 How to Compile

```bash
# Navigate to the specific version
cd versions/ai-ml

# Compile the resume
pdflatex main.tex

# Or use your preferred LaTeX compiler
```

## ✏️ How to Edit

### To update shared content (heading, education, hackathon):
Edit files in `/sections/`

### To update version-specific content:
1. **Experience**: Edit `experience.tex` in the specific version folder
2. **Projects**: Edit `projects.tex` in the specific version folder
3. **Skills**: Edit `skills.tex` in the specific version folder

### To add a new version:
1. Create new folder: `mkdir versions/new-version`
2. Copy template: `cp versions/general-swe/* versions/new-version/`
3. Customize the new files

## 💡 Pro Tips

1. **Keyword matching**: Before applying, copy job description keywords into the appropriate `skills.tex`
2. **One page rule**: Each version should stay 1 page. Swap projects, don't add more.
3. **Test compile**: Always compile and check PDF before applying
4. **Name your PDFs**: Save as `Michael_Huang_Resume_AI_ML.pdf` (not just `resume.pdf`)

## 🚀 Application Checklist

- [ ] Identified correct version for the role
- [ ] Added job-specific keywords to `skills.tex`
- [ ] Compiled PDF successfully
- [ ] Checked for typos and formatting
- [ ] Named PDF appropriately
- [ ] Ready to apply!
