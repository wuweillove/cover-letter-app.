import streamlit as st
import google.generativeai as genai
import datetime
import re
import json
from io import BytesIO
from typing import Dict, List, Optional
import time

# --- CONFIGURATION ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("⚠️ API key not configured. Please set GOOGLE_API_KEY in Streamlit secrets.")
    st.stop()

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Cover Letter Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        border-left: 4px solid #667eea;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
    }
    .copy-button {
        background-color: #28a745;
        color: white;
    }
    .keyword-badge {
        display: inline-block;
        background-color: #667eea;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.85rem;
    }
    .counter {
        font-size: 0.85rem;
        color: #666;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTANTS ---
DONATION_LINK = "https://www.buymeacoffee.com/coverletter"
MAX_RESUME_CHARS = 5000
MAX_JOB_CHARS = 5000
RATE_LIMIT_SECONDS = 10

# --- TONE CONFIGURATIONS ---
TONE_PROFILES = {
    "Professional & Formal": {
        "description": "Traditional corporate tone, suitable for established companies",
        "prompt_modifier": "formal, corporate, traditional business language"
    },
    "Confident & Assertive": {
        "description": "Bold and achievement-focused, emphasizing your value",
        "prompt_modifier": "confident, assertive, achievement-oriented, emphasizing unique value proposition"
    },
    "Friendly & Approachable": {
        "description": "Warm and personable, ideal for creative or startup environments",
        "prompt_modifier": "friendly, approachable, conversational yet professional"
    },
    "Technical & Precise": {
        "description": "Data-driven and detail-oriented for technical roles",
        "prompt_modifier": "technical, precise, data-driven, highlighting specific skills and technologies"
    },
    "Creative & Dynamic": {
        "description": "Innovative and expressive for creative industries",
        "prompt_modifier": "creative, dynamic, innovative, showcasing creative thinking"
    }
}

# --- LETTER LENGTH OPTIONS ---
LENGTH_OPTIONS = {
    "Concise (200-250 words)": 250,
    "Standard (300-350 words)": 350,
    "Detailed (400-500 words)": 500
}

# --- HELPER FUNCTIONS ---

def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    if not text:
        return ""
    # Remove potentially harmful characters while preserving formatting
    text = re.sub(r'[<>{}]', '', text)
    return text.strip()

def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    """Extract important keywords from job description."""
    if not text:
        return []
    
    # Simple keyword extraction (can be enhanced with NLP libraries)
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    
    # Common words to exclude
    stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'your',
                  'their', 'would', 'about', 'which', 'there', 'other'}
    
    # Filter and count
    word_freq = {}
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:top_n]]

def validate_inputs(resume: str, job: str) -> tuple[bool, str]:
    """Validate user inputs."""
    if not resume or not resume.strip():
        return False, "Resume cannot be empty."
    if not job or not job.strip():
        return False, "Job description cannot be empty."
    if len(resume) < 100:
        return False, "Resume seems too short. Please provide more details."
    if len(job) < 50:
        return False, "Job description seems too short. Please provide more details."
    if len(resume) > MAX_RESUME_CHARS:
        return False, f"Resume exceeds maximum length of {MAX_RESUME_CHARS} characters."
    if len(job) > MAX_JOB_CHARS:
        return False, f"Job description exceeds maximum length of {MAX_JOB_CHARS} characters."
    return True, ""

def create_enhanced_prompt(resume: str, job: str, tone: str, length: int, 
                          keywords: List[str], emphasis_areas: List[str]) -> str:
    """Create an enhanced, structured prompt for better AI generation."""
    
    tone_config = TONE_PROFILES[tone]
    emphasis = ", ".join(emphasis_areas) if emphasis_areas else "overall fit"
    
    prompt = f"""You are a professional cover letter writer with expertise in ATS optimization and recruitment.

TASK: Write a compelling, personalized cover letter that will pass ATS systems and impress hiring managers.

TONE & STYLE: {tone_config['prompt_modifier']}

TARGET LENGTH: Approximately {length} words

STRUCTURE REQUIREMENTS:
1. Opening Paragraph: Strong hook mentioning the specific role and company, expressing genuine enthusiasm
2. Body Paragraphs (2-3): 
   - Highlight relevant experiences and achievements from the resume
   - Connect skills directly to job requirements
   - Use specific examples and quantifiable results where possible
   - Naturally incorporate these key terms from the job description: {', '.join(keywords[:5])}
3. Closing Paragraph: Call to action, expressing eagerness for an interview
4. Professional sign-off

EMPHASIS AREAS: Focus particularly on {emphasis}

FORMATTING:
- Use proper business letter format
- Include [Your Name], [Your Email], [Your Phone] placeholders at the top
- Use [Date] placeholder for the date
- Include [Hiring Manager's Name/Hiring Team] and [Company Name] placeholders
- Clear paragraph breaks for readability

KEY REQUIREMENTS:
- Make it ATS-friendly by naturally incorporating relevant keywords
- Avoid clichés and generic phrases
- Show personality while maintaining professionalism
- Demonstrate research about the company (use details from job description)
- Be specific about relevant achievements
- Avoid simply repeating the resume

CANDIDATE'S RESUME:
{resume}

JOB DESCRIPTION:
{job}

Generate the cover letter now:"""
    
    return prompt

def check_rate_limit() -> bool:
    """Simple rate limiting check."""
    if 'last_generation_time' not in st.session_state:
        st.session_state.last_generation_time = 0
    
    time_since_last = time.time() - st.session_state.last_generation_time
    
    if time_since_last < RATE_LIMIT_SECONDS:
        return False
    
    st.session_state.last_generation_time = time.time()
    return True

def generate_cover_letter(resume: str, job: str, tone: str, length: int,
                         emphasis_areas: List[str]) -> Optional[str]:
    """Generate cover letter using AI with error handling."""
    try:
        # Extract keywords
        keywords = extract_keywords(job)
        
        # Create enhanced prompt
        prompt = create_enhanced_prompt(resume, job, tone, length, keywords, emphasis_areas)
        
        # Generate with retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        top_p=0.9,
                        top_k=40,
                        max_output_tokens=2048,
                    )
                )
                
                if response and response.text:
                    return response.text
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return None
        
    except Exception as e:
        st.error(f"❌ Generation failed: {str(e)}")
        if "quota" in str(e).lower():
            st.error("⚠️ API quota exceeded. Please try again later or check your API key.")
        return None

def create_txt_download(content: str) -> BytesIO:
    """Create downloadable TXT file."""
    buffer = BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)
    return buffer

# --- SESSION STATE INITIALIZATION ---
if 'generated_letters' not in st.session_state:
    st.session_state.generated_letters = []
if 'current_letter' not in st.session_state:
    st.session_state.current_letter = None
if 'draft_resume' not in st.session_state:
    st.session_state.draft_resume = ""
if 'draft_job' not in st.session_state:
    st.session_state.draft_job = ""

# --- HEADER ---
st.markdown("""
<div class="main-header">
    <h1>📄 Professional Cover Letter Builder</h1>
    <p style="font-size: 1.1rem; margin: 0;">AI-Powered • ATS-Optimized • 100% Free</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Tone selection with descriptions
    selected_tone = st.selectbox(
        "Letter Tone:",
        options=list(TONE_PROFILES.keys()),
        help="Choose the tone that best fits the company culture"
    )
    st.caption(f"💡 {TONE_PROFILES[selected_tone]['description']}")
    
    # Length selection
    selected_length_label = st.selectbox(
        "Letter Length:",
        options=list(LENGTH_OPTIONS.keys()),
        help="Shorter letters are punchier; longer letters allow more detail"
    )
    selected_length = LENGTH_OPTIONS[selected_length_label]
    
    # Emphasis areas
    st.subheader("🎯 Emphasis Areas")
    emphasis_areas = st.multiselect(
        "Focus on:",
        ["Technical Skills", "Leadership Experience", "Project Management", 
         "Team Collaboration", "Problem Solving", "Innovation",
         "Customer Focus", "Results & Metrics"],
        default=["Technical Skills"],
        help="Select areas to emphasize in your letter"
    )
    
    st.divider()
    
    # Statistics
    if st.session_state.generated_letters:
        st.metric("Letters Generated", len(st.session_state.generated_letters))
    
    st.divider()
    
    # Support section
    st.subheader("💖 Support This Project")
    st.markdown(f"""
    If this tool helps you land your dream job, consider:
    
    ☕ [**Buy Me a Coffee**]({DONATION_LINK})
    
    Your support helps keep this tool free for everyone!
    """)
    
    st.divider()
    
    # Quick tips
    with st.expander("💡 Pro Tips"):
        st.markdown("""
        **For Best Results:**
        - Include quantifiable achievements in your resume
        - Copy the complete job description
        - Select tone that matches company culture
        - Review and customize the generated letter
        - Use keywords from the job description
        """)

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs(["📝 Create Letter", "📚 History", "ℹ️ Guide"])

with tab1:
    st.subheader("Step 1️⃣: Input Your Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        resume_input = st.text_area(
            "Your Resume/Experience",
            value=st.session_state.draft_resume,
            height=300,
            placeholder="Paste your resume or relevant experience here...\n\nInclude:\n• Work experience\n• Skills\n• Achievements\n• Education",
            help=f"Maximum {MAX_RESUME_CHARS} characters"
        )
        resume_char_count = len(resume_input)
        st.markdown(f'<div class="counter">{resume_char_count}/{MAX_RESUME_CHARS} characters</div>', 
                   unsafe_allow_html=True)
        
        if resume_char_count > MAX_RESUME_CHARS * 0.9:
            st.warning("⚠️ Approaching character limit")
    
    with col2:
        job_input = st.text_area(
            "Job Description",
            value=st.session_state.draft_job,
            height=300,
            placeholder="Paste the complete job description here...\n\nInclude:\n• Role requirements\n• Responsibilities\n• Required skills\n• Company information",
            help=f"Maximum {MAX_JOB_CHARS} characters"
        )
        job_char_count = len(job_input)
        st.markdown(f'<div class="counter">{job_char_count}/{MAX_JOB_CHARS} characters</div>', 
                   unsafe_allow_html=True)
        
        if job_char_count > MAX_JOB_CHARS * 0.9:
            st.warning("⚠️ Approaching character limit")
    
    # Save draft button
    col_draft1, col_draft2 = st.columns([1, 5])
    with col_draft1:
        if st.button("💾 Save Draft"):
            st.session_state.draft_resume = resume_input
            st.session_state.draft_job = job_input
            st.success("✅ Draft saved!")
    
    st.divider()
    
    # Keyword preview
    if job_input:
        with st.expander("🔍 Detected Keywords from Job Description"):
            keywords = extract_keywords(job_input, 15)
            if keywords:
                keyword_html = "".join([f'<span class="keyword-badge">{k}</span>' for k in keywords])
                st.markdown(keyword_html, unsafe_allow_html=True)
                st.caption("✨ These keywords will be naturally incorporated into your letter for ATS optimization")
    
    st.divider()
    st.subheader("Step 2️⃣: Generate Your Cover Letter")
    
    # Generate button
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
    with col_btn2:
        generate_clicked = st.button("🚀 Generate Letter", type="primary", use_container_width=True)
    
    if generate_clicked:
        # Sanitize inputs
        resume_clean = sanitize_input(resume_input)
        job_clean = sanitize_input(job_input)
        
        # Validate
        is_valid, error_msg = validate_inputs(resume_clean, job_clean)
        
        if not is_valid:
            st.error(f"❌ {error_msg}")
        elif not check_rate_limit():
            st.warning(f"⏳ Please wait {RATE_LIMIT_SECONDS} seconds between generations to prevent abuse.")
        else:
            # Log generation event
            print(f"[{datetime.datetime.now()}] 💰 Letter generated - Tone: {selected_tone}, Length: {selected_length}")
            
            # Generate with progress
            with st.spinner("✨ Crafting your personalized cover letter..."):
                progress_bar = st.progress(0)
                progress_bar.progress(25)
                
                result = generate_cover_letter(
                    resume_clean,
                    job_clean,
                    selected_tone,
                    selected_length,
                    emphasis_areas
                )
                
                progress_bar.progress(100)
                
                if result:
                    st.session_state.current_letter = result
                    st.session_state.generated_letters.append({
                        'content': result,
                        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'tone': selected_tone,
                        'length': selected_length_label
                    })
                    st.success("✅ Your cover letter is ready!")
                else:
                    st.error("❌ Failed to generate letter. Please try again.")
    
    # Display current letter
    if st.session_state.current_letter:
        st.divider()
        st.subheader("📄 Your Generated Cover Letter")
        
        # Editable text area
        edited_letter = st.text_area(
            "Review and edit your letter:",
            value=st.session_state.current_letter,
            height=500,
            help="You can edit the generated letter directly here"
        )
        
        # Update session state if edited
        if edited_letter != st.session_state.current_letter:
            st.session_state.current_letter = edited_letter
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.download_button(
                label="📥 Download TXT",
                data=create_txt_download(st.session_state.current_letter),
                file_name=f"cover_letter_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col2:
            # Copy to clipboard button (uses Streamlit's built-in functionality)
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(st.session_state.current_letter, language=None)
                st.success("✅ Letter displayed above - copy using Ctrl+C / Cmd+C")
        
        with col3:
            if st.button("🔄 Generate Another", use_container_width=True):
                st.session_state.current_letter = None
                st.rerun()
        
        with col4:
            st.markdown(f'<a href="{DONATION_LINK}" target="_blank"><button style="width:100%; padding:0.5rem; background-color:#FFDD00; border:none; border-radius:8px; cursor:pointer; font-weight:600;">☕ Donate</button></a>', 
                       unsafe_allow_html=True)
        
        # Word count
        word_count = len(st.session_state.current_letter.split())
        st.caption(f"📊 Word count: {word_count} words")

with tab2:
    st.subheader("📚 Generation History")
    
    if not st.session_state.generated_letters:
        st.info("💡 No letters generated yet. Create your first cover letter in the 'Create Letter' tab!")
    else:
        st.success(f"✅ You have generated {len(st.session_state.generated_letters)} letter(s)")
        
        for idx, letter in enumerate(reversed(st.session_state.generated_letters)):
            with st.expander(f"Letter #{len(st.session_state.generated_letters) - idx} - {letter['timestamp']} ({letter['tone']})"):
                st.text_area(
                    "Content:",
                    value=letter['content'],
                    height=300,
                    key=f"history_{idx}",
                    disabled=True
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"📥 Download", key=f"download_{idx}"):
                        st.download_button(
                            label="Download TXT",
                            data=create_txt_download(letter['content']),
                            file_name=f"cover_letter_{letter['timestamp'].replace(':', '-')}.txt",
                            mime="text/plain",
                            key=f"download_btn_{idx}"
                        )
                with col2:
                    if st.button(f"🔄 Use as Template", key=f"template_{idx}"):
                        st.session_state.current_letter = letter['content']
                        st.success("✅ Loaded to editor!")
        
        # Clear history button
        st.divider()
        if st.button("🗑️ Clear All History", type="secondary"):
            st.session_state.generated_letters = []
            st.success("✅ History cleared!")
            st.rerun()

with tab3:
    st.subheader("📖 How to Use This Tool")
    
    st.markdown("""
    ### 🎯 Quick Start Guide
    
    1. **Prepare Your Resume**: Copy your resume or relevant work experience
    2. **Get Job Description**: Copy the complete job posting you're applying for
    3. **Choose Settings**: Select tone, length, and emphasis areas in the sidebar
    4. **Generate**: Click the generate button and wait for your personalized letter
    5. **Review & Edit**: Customize the generated letter to add your personal touch
    6. **Download**: Save your letter in your preferred format
    
    ### ✨ Best Practices
    
    **Resume Input:**
    - Include specific achievements with numbers (e.g., "Increased sales by 35%")
    - List relevant skills and technologies
    - Mention certifications and education
    - Keep it concise but comprehensive
    
    **Job Description:**
    - Copy the entire job posting
    - Include company information if available
    - Don't edit or summarize - let the AI identify key points
    
    **Tone Selection:**
    - **Professional & Formal**: Traditional corporate environments, finance, law
    - **Confident & Assertive**: Leadership roles, competitive industries
    - **Friendly & Approachable**: Startups, creative agencies, casual cultures
    - **Technical & Precise**: Engineering, data science, IT roles
    - **Creative & Dynamic**: Marketing, design, media, creative fields
    
    ### 🔐 Privacy & Security
    
    - Your data is processed securely through Google's Gemini API
    - No personal information is stored permanently
    - Generated letters are kept only in your browser session
    - Clear your browser cache to remove all data
    
    ### 🚀 Pro Tips
    
    - **Customize keywords**: Make sure the job description includes the specific keywords you want to highlight
    - **Multiple versions**: Generate several versions and combine the best parts
    - **Personal touch**: Always add a specific detail about why you're interested in THIS company
    - **Proofread**: AI is great, but human review is essential
    - **ATS optimization**: The tool naturally incorporates keywords for ATS systems
    
    ### ⚠️ Important Notes
    
    - **Review carefully**: AI-generated content may need adjustments
    - **Add specifics**: Include specific company details you've researched
    - **Be authentic**: Use the generated letter as a starting point, not the final product
    - **Update placeholders**: Replace [Your Name], [Date], etc. with actual information
    
    ### 📞 Need Help?
    
    If you encounter issues:
    - Check that both resume and job description are filled
    - Ensure you're not exceeding character limits
    - Wait at least 10 seconds between generations
    - Try refreshing the page if something seems stuck
    
    ### 💖 Support
    
    This tool is completely free to use. If it helps you land a job interview, consider supporting:
    ☕ [Buy Me a Coffee]({DONATION_LINK})
    
    ---
    
    **Version 2.0** - Enhanced with AI-powered keyword extraction, multiple tone options, ATS optimization, and more!
    """)

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Made with ❤️ for job seekers everywhere | <a href="{}" target="_blank">Support this project</a></p>
    <p style="font-size: 0.85rem;">Powered by Google Gemini AI • Built with Streamlit</p>
</div>
""".format(DONATION_LINK), unsafe_allow_html=True)
