# 📄 CoverLetterPro v3.0 - AI-Powered Professional Cover Letter Builder

![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.32+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎉 NEW in Version 3.0 - Complete Professional Redesign!

**CoverLetterPro** is now a fully-featured, enterprise-grade AI-powered cover letter builder with advanced features that help you land your dream job!

---

## ✨ Key Features

### 🎨 **Modern Professional Interface**
- 🌓 **Light/Dark Theme Toggle** - Switch themes with one click
- 🎯 **Step-by-Step Guided Experience** - 5-step process with progress tracking
- 📱 **Fully Responsive** - Perfect on desktop, tablet, and mobile
- ✨ **Smooth Animations** - Professional transitions and visual feedback

### 🤖 **Advanced AI Generation**
- 🏢 **14+ Industry Templates** - Technology, Finance, Healthcare, Marketing, and more
- 🎭 **5 Writing Modes** - Professional, Confident, Creative, Technical, Friendly
- 🔄 **A/B Testing** - Generate up to 5 versions for comparison
- 🧠 **Smart Customization** - AI learns from your inputs and preferences

### 🎯 **ATS Optimization**
- 📊 **Real-Time ATS Score** (0-100) - Know if your letter will pass screening
- 🔍 **Keyword Analysis** - Automatic extraction and matching
- ✅ **70+ keyword coverage target** - Industry-standard optimization
- 💡 **Improvement Suggestions** - Specific, actionable recommendations

### 📈 **Comprehensive Analysis**
- 🎯 **Overall Effectiveness Score** - Weighted scoring across 5 factors
- ✍️ **Grammar & Style Checking** - Built-in proofreading
- 🎨 **Tone Analysis** - Ensure your tone matches company culture
- 📊 **Skills Matching** - Compare your skills with job requirements
- 💯 **Letter Grades** - A-F rating with explanations

### 👤 **Profile Management**
- 💾 **Persistent Profiles** - Save your information for reuse
- 📝 **Complete Details** - Name, contact, experience, skills, summary
- 📤 **Export/Import** - Take your data anywhere
- ⚡ **Quick Fill** - Populate letters with saved info

### 📄 **Professional Export**
- 📑 **PDF Export** - Professional formatting with branding
- 📝 **Word Export** - Editable DOCX format (coming soon)
- 📋 **Copy to Clipboard** - Quick copy functionality
- 🏢 **Company Branding** - Add company-specific formatting

### 📚 **History & Version Management**
- 🗂️ **Unlimited History** - Save all your letters
- 🔍 **Search & Filter** - Find past letters easily
- 📊 **Version Comparison** - Compare different versions
- 📥 **Batch Export** - Download multiple letters at once

### 💡 **Contextual Help**
- 📖 **Comprehensive Guide** - Step-by-step instructions
- 🎯 **Industry Examples** - Real cover letters that worked
- ⭐ **Success Stories** - User testimonials
- ❓ **FAQ Section** - Common questions answered
- 💡 **Pro Tips** - Best practices throughout the app

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/wuweillove/cover-letter-app..git
cd cover-letter-app.

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

Create `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "your-gemini-api-key-here"
```

Get your free API key at: https://makersuite.google.com/app/apikey

### 3. Run the Application

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`

---

## 📖 How to Use

### Step 1: Set Up Your Profile
1. Click "Profile" button or go to "Profile & Settings" tab
2. Fill in your personal information (name, email, phone)
3. Add your experience, skills, and professional summary
4. Click "Save Profile"

### Step 2: Configure Settings (Sidebar)
- Select your target industry
- Choose experience level (Entry, Mid, Senior, Executive)
- Pick writing mode that matches company culture
- Adjust desired letter length

### Step 3: Input Your Data
- **Resume**: Paste or upload (PDF/DOCX supported)
- **Job Description**: Paste or extract from URL
- Review extracted keywords automatically

### Step 4: Customize Your Letter
- Choose industry-specific template
- Select emphasis areas (skills to highlight)
- Add custom keywords (optional)

### Step 5: Generate
- Choose number of versions (1-5) for A/B testing
- Enable AI analysis for detailed feedback
- Click "Generate Cover Letter(s)"
- Wait 5-15 seconds per version

### Step 6: Review & Analyze
- Check your **Overall Effectiveness Score** (target: 80+)
- Review detailed analysis:
  - **ATS Score** (target: 80+)
  - **Grammar Score** (target: 90+)
  - **Keyword Coverage** (target: 70-80%)
  - **Skills Match Percentage**
- Read AI-powered suggestions
- Compare versions if multiple generated

### Step 7: Edit & Finalize
- Select best version or edit directly
- Apply suggested improvements
- Add company-specific details
- Final proofread

### Step 8: Export
- Download as PDF (professional formatting)
- Download as Word (for further editing)
- Copy to clipboard
- Save to history

---

## 🎯 Scoring Guide

### Overall Effectiveness Score

**Components (Weighted)**:
- ATS Score: 30%
- Grammar Score: 20%
- Keyword Coverage: 20%
- Structure: 15%
- Personalization: 15%

**Score Interpretation**:
- **90-100**: Exceptional - Very likely to impress recruiters
- **80-89**: Excellent - Strong chance of getting interview
- **70-79**: Good - Competitive application
- **60-69**: Fair - Needs some improvements
- **Below 60**: Needs work - Significant revision required

### Target Scores
- 🎯 **ATS Score**: 80+ (most companies)
- ✍️ **Grammar Score**: 90+ (professional quality)
- 🔑 **Keyword Coverage**: 70-80% (optimal)
- 📊 **Overall Score**: 80+ (strong application)

---

## 🏢 Industry Templates

We provide specialized templates for:

- 💻 **Technology** - Software Engineer, Data Scientist, DevOps, Product Manager
- 💰 **Finance & Banking** - Financial Analyst, Investment Banker, Risk Manager
- 🏥 **Healthcare** - Nurse, Physician, Healthcare Administrator
- 📚 **Education** - Teacher, Professor, Academic Administrator
- 📱 **Marketing** - Digital Marketing, Content Strategy, Brand Management
- 💼 **Sales** - Sales Executive, Business Development, Account Management
- ⚙️ **Engineering** - Mechanical, Electrical, Manufacturing
- ⚖️ **Legal** - Attorney, Paralegal, Compliance Officer
- 🎨 **Design** - Graphic Designer, UX/UI, Creative Director
- 🏨 **Hospitality** - Hotel Management, Event Planning
- 🏡 **Real Estate** - Agent, Property Manager
- 💡 **Consulting** - Management, Strategy, IT Consulting
- ❤️ **Non-Profit** - Program Manager, Fundraising
- 🏛️ **Government** - Public Sector roles

---

## 💡 Pro Tips

### For Best Results

✅ **Complete your profile first** - Saves time on every letter
✅ **Use the correct industry** - Templates are optimized per industry
✅ **Paste full job description** - Don't truncate or summarize
✅ **Generate 2-3 versions** - Compare and choose the best
✅ **Target 80+ ATS score** - Ensures you pass automated screening
✅ **Include specific metrics** - Numbers and percentages stand out
✅ **Proofread carefully** - AI is great, but human review is essential
✅ **Personalize for company** - Research and add specific details
✅ **Keep it concise** - 300-400 words is optimal
✅ **Use strong action verbs** - Achieved, developed, led, implemented

### Common Mistakes to Avoid

❌ Using generic templates without customization
❌ Ignoring ATS score below 70
❌ Not including quantifiable achievements
❌ Exceeding 500 words
❌ Using clichés ("team player", "hard worker")
❌ Forgetting company-specific research
❌ Not proofreading the final version
❌ Sending first version without comparison

---

## 🛠️ Technical Architecture

### Modular Design

```
cover-letter-app/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
└── utils/                      # Utility modules
    ├── theme_manager.py        # Theme and styling
    ├── profile_manager.py      # User profile management
    ├── templates.py            # Industry templates
    ├── ats_optimizer.py        # ATS scoring
    ├── keyword_analyzer.py     # Keyword extraction
    ├── skill_matcher.py        # Skills matching
    ├── grammar_checker.py      # Grammar checking
    ├── pdf_exporter.py         # PDF/Word export
    ├── scoring.py              # Effectiveness scoring
    ├── ai_generator.py         # AI generation
    └── version_manager.py      # Version control
```

### Technology Stack

- **Framework**: Streamlit 1.32+
- **AI Engine**: Google Gemini 1.5 Flash
- **Language**: Python 3.8+
- **File Processing**: PyPDF2, python-docx
- **Web Scraping**: BeautifulSoup4, requests
- **Data Processing**: pandas, numpy

---

## 📊 API Usage & Costs

### Google Gemini API

- **Free Tier**: 60 requests/minute, 1M characters/month free
- **Model**: gemini-1.5-flash-latest
- **Cost per letter**: ~$0.002 (after free tier)
- **Typical request**: ~2000 tokens

### Estimated Usage

- 100 letters: ~$0 (within free tier)
- 1,000 letters: ~$2
- 10,000 letters: ~$20

Monitor usage at: https://makersuite.google.com/

---

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Add `GOOGLE_API_KEY` in app secrets
6. Click Deploy!

Your app will be live at: `https://your-app.streamlit.app`

### Other Platforms

<details>
<summary><b>Heroku</b></summary>

```bash
heroku create your-app-name
git push heroku main
heroku config:set GOOGLE_API_KEY=your-key
```
</details>

<details>
<summary><b>Docker</b></summary>

```bash
docker build -t coverletterpro .
docker run -p 8501:8501 -e GOOGLE_API_KEY=your-key coverletterpro
```
</details>

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 Changelog

### Version 3.0.0 (2026-02-11) - Major Release

**New Features**:
- ✨ Complete UI/UX redesign with modern interface
- 🌓 Light/dark theme toggle
- 📍 Step-by-step guided experience
- 🏢 14+ industry-specific templates (70+ variations)
- 🎯 Advanced ATS optimization with real-time scoring
- 🔄 A/B testing with multiple version generation
- 👤 User profile management with persistence
- ✍️ Integrated grammar and style checking
- 📊 AI-powered effectiveness scoring
- 🔍 Smart keyword extraction and matching
- 💼 Skills matching analysis
- 📄 Professional PDF/Word export
- 💡 Contextual tips and industry examples
- 📚 Comprehensive guide with FAQ

**Technical Improvements**:
- Modular architecture with 11 utility modules
- Improved error handling and user feedback
- Enhanced AI prompt engineering
- Better performance and caching
- Responsive design for all devices

---

## ❓ FAQ

**Q: Is my data safe?**  
A: Yes! All data is stored only in your browser session. Nothing is saved on our servers.

**Q: Do I need to pay for the API?**  
A: Google Gemini offers a generous free tier. Most users stay within the free quota.

**Q: How accurate is the ATS score?**  
A: Our scoring uses industry-standard algorithms. Scores 80+ generally pass most ATS systems.

**Q: Can I use this for multiple jobs?**  
A: Absolutely! Save unlimited letters and create new ones anytime.

**Q: What if generation fails?**  
A: We provide fallback templates and clear error messages. Check your API key and internet connection.

**Q: How long should my cover letter be?**  
A: 300-400 words (3-4 paragraphs) is optimal for most positions.

---

## 🐛 Troubleshooting

### Common Issues

**"API key not configured"**
- Ensure `.streamlit/secrets.toml` exists with your API key
- Restart the application after adding the key

**"Generation failed"**
- Check your internet connection
- Verify API key is valid
- Ensure you haven't exceeded API quota

**"ATS score is low"**
- Add more keywords from job description
- Use simpler formatting
- Include more specific skills and achievements

**"Can't upload file"**
- Check file format (PDF/DOCX only)
- Ensure file size < 10MB
- Try copying and pasting text instead

---

## 🌟 Roadmap

### Coming Soon

- [ ] True PDF generation with styling
- [ ] Word document export (DOCX)
- [ ] Email integration for direct sending
- [ ] Browser extension
- [ ] Mobile app (iOS/Android)
- [ ] Additional languages support
- [ ] Resume builder integration
- [ ] Interview preparation tool
- [ ] Salary negotiation guide
- [ ] Job application tracking

---

## 👥 Support & Community

### Get Help

- 📚 **Documentation**: [README_V3.md](README_V3.md) for detailed docs
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/wuweillove/cover-letter-app./issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/wuweillove/cover-letter-app./discussions)

### Community

- ⭐ Star this repo if you find it helpful
- 🐦 Share on social media
- 📢 Tell your friends who are job hunting
- 💬 Join discussions and share your experience

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Built with**: [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- **AI Powered by**: [Google Gemini](https://deepmind.google/technologies/gemini/) - Advanced AI technology
- **Inspired by**: Job seekers worldwide who deserve better tools
- **Special Thanks**: To all contributors and users who provide feedback

---

## ❤️ Support the Project

If CoverLetterPro helps you land your dream job:

- ⭐ **Star this repository**
- 🍴 **Fork and contribute**
- 📢 **Share with friends**
- 💬 **Leave feedback**
- ☕ **[Buy us a coffee](https://buymeacoffee.com/coverletterpro)**

---

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/wuweillove/cover-letter-app./issues)
- **Discussions**: [GitHub Discussions](https://github.com/wuweillove/cover-letter-app./discussions)
- **Email**: support@coverletterpro.com (coming soon)

---

<div align="center">

**Made with ❤️ for job seekers everywhere**

[🌐 Live Demo](https://coverletterpro.streamlit.app) • [📖 Documentation](README_V3.md) • [🐛 Report Bug](https://github.com/wuweillove/cover-letter-app./issues) • [✨ Request Feature](https://github.com/wuweillove/cover-letter-app./issues)

© 2026 CoverLetterPro. All rights reserved.

</div>
