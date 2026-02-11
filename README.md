# 📄 Professional Cover Letter Builder

An AI-powered, ATS-optimized cover letter generator built with Streamlit and Google Gemini AI. Create personalized, professional cover letters in seconds!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

### 🎨 Enhanced UI/UX
- **Modern Design**: Beautiful gradient headers and professional styling
- **Three-Tab Interface**: Organized workflow with Create, History, and Guide sections
- **Real-time Feedback**: Character counters, progress bars, and status indicators
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Dark Mode Ready**: Customizable theme settings

### 🤖 Advanced AI Generation
- **Multiple Tone Options**: 5 different professional tones to match company culture
  - Professional & Formal
  - Confident & Assertive
  - Friendly & Approachable
  - Technical & Precise
  - Creative & Dynamic
- **Intelligent Keyword Extraction**: Automatically identifies and incorporates key terms from job descriptions
- **ATS Optimization**: Letters formatted to pass Applicant Tracking Systems
- **Customizable Length**: Choose from concise (200-250 words), standard (300-350 words), or detailed (400-500 words)
- **Emphasis Areas**: Focus on specific skills like Technical Skills, Leadership, Innovation, etc.
- **Advanced Prompt Engineering**: Structured prompts for consistent, high-quality results

### 💾 Productivity Features
- **Draft Saving**: Save your inputs for later use
- **Generation History**: Keep track of all generated letters
- **Editable Output**: Modify AI-generated content directly in the app
- **Multiple Downloads**: Export as TXT (PDF and DOCX support coming soon)
- **Copy to Clipboard**: Quick copy functionality
- **Template Reuse**: Load previous letters as templates

### 🔒 Security & Reliability
- **Input Validation**: Comprehensive checks for data quality
- **Input Sanitization**: Protection against injection attacks
- **Rate Limiting**: Prevents abuse with 10-second cooldown between generations
- **Error Handling**: Graceful failure recovery with user-friendly messages
- **Secure Configuration**: API keys managed through Streamlit secrets
- **Retry Logic**: Automatic retries with exponential backoff

### 📊 Smart Analytics
- **Keyword Detection**: Visual display of extracted keywords from job descriptions
- **Word Count**: Real-time tracking of letter length
- **Generation Counter**: Track how many letters you've created
- **Usage Insights**: Understand your usage patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wuweillove/cover-letter-app..git
   cd cover-letter-app.
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   
   Create a file `.streamlit/secrets.toml` with:
   ```toml
   GOOGLE_API_KEY = "your-api-key-here"
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Connect your GitHub account** and select this repository

4. **Add your API key** in the Streamlit Cloud secrets:
   - Go to App Settings → Secrets
   - Add: `GOOGLE_API_KEY = "your-api-key-here"`

5. **Deploy!** Your app will be live in minutes

### Other Platforms

<details>
<summary>Deploy to Heroku</summary>

1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```

2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku config:set GOOGLE_API_KEY=your-api-key
   ```
</details>

<details>
<summary>Deploy to Docker</summary>

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py"]
   ```

2. Build and run:
   ```bash
   docker build -t cover-letter-app .
   docker run -p 8501:8501 -e GOOGLE_API_KEY=your-key cover-letter-app
   ```
</details>

## 📖 Usage Guide

### Basic Workflow

1. **Prepare Your Information**
   - Copy your resume or relevant experience
   - Get the complete job description you're applying for

2. **Configure Settings** (Sidebar)
   - Choose the appropriate tone for the company
   - Select desired letter length
   - Pick emphasis areas to highlight

3. **Input Your Data**
   - Paste resume in the left text area
   - Paste job description in the right text area
   - Review detected keywords

4. **Generate**
   - Click "Generate Letter"
   - Wait for AI to craft your letter (usually 5-10 seconds)

5. **Review & Edit**
   - Customize the generated content
   - Check word count and formatting
   - Make it personal with specific company details

6. **Download**
   - Choose your preferred format
   - Copy to clipboard or download file

### Pro Tips

✅ **For Best Results:**
- Include quantifiable achievements in your resume (e.g., "Increased sales by 35%")
- Copy the complete, unedited job description
- Select a tone that matches the company culture
- Always add a personal touch about the specific company
- Proofread and customize the generated letter

✅ **Tone Selection Guide:**
- **Startups/Creative**: Friendly & Approachable or Creative & Dynamic
- **Corporate/Finance**: Professional & Formal
- **Tech/Engineering**: Technical & Precise
- **Leadership Roles**: Confident & Assertive

✅ **ATS Optimization:**
- The tool automatically incorporates keywords from the job description
- Uses clear formatting that ATS systems can parse
- Includes relevant skills and qualifications prominently

## 🛠️ Technical Architecture

### Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: Google Gemini 1.5 Flash
- **Language**: Python 3.8+
- **Styling**: Custom CSS with gradient themes

### Key Components

```
app.py                    # Main application
├── Configuration         # API setup, constants, tone profiles
├── Helper Functions      # Sanitization, validation, keyword extraction
├── AI Generation         # Enhanced prompt engineering, retry logic
├── Session State         # Draft saving, history management
└── UI Components         # Three-tab interface, forms, buttons
```

### Security Features
- Input sanitization to prevent injection
- Rate limiting (10 seconds between requests)
- Secure API key management via secrets
- XSRF protection enabled
- No permanent data storage

### Performance Optimizations
- Session state for quick access to history
- Lazy loading of AI model
- Efficient keyword extraction algorithm
- Minimal external dependencies

## 🔧 Configuration

### Environment Variables

Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your-google-gemini-api-key"
```

### Customization Options

**Modify Tone Profiles** (`app.py`, line 59):
```python
TONE_PROFILES = {
    "Your Custom Tone": {
        "description": "Description here",
        "prompt_modifier": "tone instructions for AI"
    }
}
```

**Adjust Rate Limiting** (`app.py`, line 56):
```python
RATE_LIMIT_SECONDS = 10  # Change to your preference
```

**Change AI Model** (`app.py`, line 194):
```python
model = genai.GenerativeModel('gemini-1.5-flash')  # Try other models
```

## 📊 API Usage & Costs

### Google Gemini API
- **Free Tier**: 60 requests per minute
- **Cost**: First 1M characters free per month
- **Typical Letter**: ~1,500 characters = ~0.0015 API units
- **Monitor Usage**: Check [Google AI Studio](https://makersuite.google.com/)

### Estimated Costs
- 100 letters: ~$0 (within free tier)
- 1,000 letters: ~$0.15
- 10,000 letters: ~$1.50

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
1. Check existing [Issues](https://github.com/wuweillove/cover-letter-app./issues)
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features
1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Include examples or mockups if possible

### Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/cover-letter-app..git
cd cover-letter-app.

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
pytest

# Start development server
streamlit run app.py
```

## 📝 Changelog

### Version 2.0.0 (Current)
- ✨ Complete UI/UX overhaul with modern design
- 🤖 Enhanced AI generation with 5 tone options
- 🔍 Intelligent keyword extraction from job descriptions
- 💾 Draft saving and generation history
- ✏️ Editable output with real-time updates
- 🎯 Customizable emphasis areas
- 📏 Multiple letter length options
- 🔒 Improved security with input validation and rate limiting
- 📊 Real-time statistics and analytics
- 📖 Comprehensive user guide and tips
- 🎨 Custom CSS styling and theming
- ⚡ Better error handling and retry logic

### Version 1.0.0 (Original)
- Basic cover letter generation
- Simple two-column input layout
- Three tone options
- Google Gemini integration

## 🐛 Troubleshooting

### Common Issues

**"API key not configured"**
- Ensure `.streamlit/secrets.toml` exists with your API key
- Check key format: `GOOGLE_API_KEY = "your-key"`
- Restart the application after adding the key

**"Rate limit exceeded"**
- Wait 10 seconds between generations
- Check Google API quota in console

**"Generation failed"**
- Verify your API key is valid
- Check internet connection
- Ensure inputs are not empty
- Try refreshing the page

**Character limit warnings**
- Resume: max 5,000 characters
- Job description: max 5,000 characters
- Summarize if needed while keeping key information

**Slow generation**
- Normal generation time: 5-15 seconds
- Check internet speed
- Google API may be experiencing high load

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 Cover Letter Pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Inspired by job seekers worldwide

## 💖 Support

This tool is **100% free** to use. If it helps you land a job interview or offer, consider:

☕ [**Buy Me a Coffee**](https://www.buymeacoffee.com/coverletter)

Your support helps keep this tool free for everyone!

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/wuweillove/cover-letter-app./issues)
- **Discussions**: [GitHub Discussions](https://github.com/wuweillove/cover-letter-app./discussions)

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ for job seekers everywhere**

