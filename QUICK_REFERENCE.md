# Quick Reference Card

## 🎯 Which Resume to Use?

| Keywords in Job Posting | Use This |
|------------------------|----------|
| AI, ML, PyTorch, LLM, Deep Learning | `ai-ml` |
| React, Node, Full-Stack, MERN | `fullstack` |
| Backend, APIs, Systems, Linux | `backend` |
| General SWE, New Grad | `general-swe` |

## ⚡ Common Commands

### Compile a Resume
```bash
cd versions/ai-ml
pdflatex main.tex
open main.pdf
```

### Compile All Versions
```bash
cd versions
for v in ai-ml fullstack backend general-swe; do
  cd $v && pdflatex main.tex && cd ..
done
```

### Rename for Application
```bash
cp versions/ai-ml/main.pdf ~/Desktop/Michael_Huang_Resume_AI_ML.pdf
```

## 📝 What to Edit

| To Change... | Edit This File |
|-------------|----------------|
| Contact info | `sections/heading.tex` |
| Education | `sections/education.tex` |
| Hackathon | `sections/hackathon.tex` |
| Experience (AI/ML) | `versions/ai-ml/experience.tex` |
| Projects (AI/ML) | `versions/ai-ml/projects.tex` |
| Skills (AI/ML) | `versions/ai-ml/skills.tex` |
| Formatting | `preamble.tex` |

After editing shared files (`sections/*` or `preamble.tex`), recompile ALL versions.
After editing version-specific files, recompile just that version.

## 🔄 Application Workflow

1. Read job description → Find key technologies
2. Choose resume version → Match technologies
3. Edit `skills.tex` → Add missing keywords (if you have that skill)
4. Compile → `pdflatex main.tex`
5. Rename → `Michael_Huang_Resume_[Type].pdf`
6. Apply → Company website (not just LinkedIn)
7. Track → Add to `APPLICATION_TRACKER.md`
8. Follow up → 1 week later if no response

## 📊 Success Metrics

- **Applications per week**: 10-15 (quality over quantity)
- **Target response rate**: 20-30%
- **Best application times**: Mon-Wed, 6-10 AM PT
- **Follow up after**: 1 week

## 🐛 Quick Fixes

**pdflatex not found?**
```bash
export PATH="/Library/TeX/texbin:$PATH"
```

**Changes not showing?**
```bash
rm *.aux *.log *.out
pdflatex main.tex
```

**Resume too long?**
- Remove a bullet point or project
- Never go below 11pt font
- Keep to 1 page

## 💡 Remember

- ✅ Quantify achievements with numbers
- ✅ Mirror job description keywords
- ✅ Apply directly on company website
- ✅ Track every application
- ✅ Follow up after 1 week
- ❌ Don't use generic resumes
- ❌ Don't exceed 1 page
- ❌ Don't apply to 100+ jobs blindly

---

**Full documentation**: See `README.md`
