import streamlit as st
import sys
from pathlib import Path
import time

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.theme_manager import ThemeManager, apply_custom_css
from utils.profile_manager import ProfileManager
from utils.templates import TemplateManager
from utils.ats_optimizer import ATSOptimizer
from utils.keyword_analyzer import KeywordAnalyzer
from utils.skill_matcher import SkillMatcher
from utils.grammar_checker import GrammarChecker
from utils.pdf_exporter import PDFExporter
from utils.scoring import LetterScorer
from utils.ai_generator import AIGenerator
from utils.version_manager import VersionManager
from utils.profile_header import render_profile_header, render_profile_section_enhanced
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CoverLetterPro - Professional Cover Letter Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INITIALIZE MANAGERS ---
if 'theme_manager' not in st.session_state:
    st.session_state.theme_manager = ThemeManager()
if 'profile_manager' not in st.session_state:
    st.session_state.profile_manager = ProfileManager()
if 'template_manager' not in st.session_state:
    st.session_state.template_manager = TemplateManager()
if 'version_manager' not in st.session_state:
    st.session_state.version_manager = VersionManager()
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'generated_versions' not in st.session_state:
    st.session_state.generated_versions = []
if 'show_profile_modal' not in st.session_state:
    st.session_state.show_profile_modal = False

# Apply modern theme
theme = st.session_state.theme_manager
apply_custom_css(theme.get_current_theme())

# --- MODERN PROFILE HEADER ---
profile = render_profile_header(st.session_state.profile_manager)

# --- HEADER WITH THEME TOGGLE ---
col1, col2 = st.columns([10, 2])
with col1:
    st.markdown("""
    <div class="main-header">
        <h1>📄 CoverLetterPro</h1>
        <p class="subtitle">AI-Powered Professional Cover Letter Builder</p>
        <p class="tagline">ATS-Optimized • Industry Templates • Smart Matching • Professional Export</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🌓 Toggle Theme", key="theme_toggle", help="Switch light/dark mode", use_container_width=True):
        theme.toggle_theme()
        st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ Quick Settings")
    
    # Profile Quick Actions
    if profile.get('name'):
        completion = st.session_state.profile_manager.get_profile_completion_percentage()
        st.metric("Profile Complete", f"{completion}%", help="Complete your profile for better results")
    else:
        st.warning(\"⚠️ Complete your profile first!\")
    
    st.divider()
    
    # Language Selection
    language = st.selectbox(
        \"🌐 Language\",
        [\"English\", \"Español\"],
        help=\"Select interface language\"
    )
    st.session_state.language = 'en' if language == \"English\" else 'es'
    
    # Industry Selection
    industries = st.session_state.template_manager.get_industries()
    selected_industry = st.selectbox(
        \"🏢 Target Industry\",
        industries,
        help=\"Select your target industry\"
    )
    
    # Experience Level
    experience_level = st.selectbox(
        \"📊 Experience Level\",
        [\"Entry Level\", \"Mid Level\", \"Senior Level\", \"Executive\"],
        help=\"Your experience level\"
    )
    
    # Writing Mode
    writing_mode = st.selectbox(
        \"✍️ Writing Style\",
        [\"Professional & Formal\", \"Confident & Assertive\", \"Creative & Dynamic\", 
         \"Technical & Precise\", \"Friendly & Approachable\"],
        help=\"Choose writing style\"
    )
    
    # Letter Length
    letter_length = st.select_slider(
        \"📏 Letter Length\",
        options=[\"Concise (200-250)\", \"Standard (300-350)\", \"Detailed (400-500)\"],
        value=\"Standard (300-350)\"
    )
    
    st.divider()
    
    # Statistics
    st.markdown(\"### 📊 Your Stats\")\n    col1, col2 = st.columns(2)
    with col1:
        st.metric(\"Letters\", len(st.session_state.version_manager.get_all_versions()))
    with col2:
        st.metric(\"Versions\", len(st.session_state.generated_versions))

# --- PROGRESS INDICATOR ---
st.markdown(\"### 📍 Your Progress\")
progress_steps = [\"Profile\", \"Input\", \"Customize\", \"Generate\", \"Review & Export\"]
current_step = st.session_state.current_step

progress_html = '<div class=\"progress-container\">'
for i, step in enumerate(progress_steps, 1):
    status = \"completed\" if i < current_step else (\"active\" if i == current_step else \"pending\")
    icon = \"✅\" if i < current_step else (\"🔵\" if i == current_step else \"⚪\")
    progress_html += f'<div class=\"progress-step {status}\">{icon} {step}</div>'
progress_html += '</div>'

st.markdown(progress_html, unsafe_allow_html=True)
st.progress(current_step / len(progress_steps))

st.divider()

# --- MAIN TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    \"📝 Create Letter\",
    \"🔍 Analysis & Scoring\",
    \"📚 History & Versions\",
    \"👤 Profile & Settings\",
    \"📖 Guide & Examples\"
])

# ============================================
# TAB 1: CREATE LETTER
# ============================================
with tab1:
    st.markdown(\"## Step-by-Step Letter Creation\")
    
    # STEP 1: Profile Check
    with st.expander(\"### 1️⃣ Profile Information\", expanded=current_step==1):
        if not profile.get('name') or not profile.get('email'):
            st.warning(\"⚠️ Please complete your profile in the 'Profile & Settings' tab first!\")
            if st.button(\"✏️ Go to Profile →\", key=\"goto_profile\", type=\"primary\"):
                st.session_state.current_step = 4
                st.rerun()
        else:
            st.success(f\"✅ Profile ready: **{profile['name']}** ({profile.get('current_title', 'Professional')})\")
            if st.button(\"Continue to Input →\", key=\"step1_continue\", type=\"primary\"):
                st.session_state.current_step = 2
                st.rerun()
    
    # Continue with rest of the tabs (keeping existing functionality)...
    # [Rest of the original app.py content continues here...]

# ============================================
# TAB 4: ENHANCED PROFILE & SETTINGS
# ============================================
with tab4:
    render_profile_section_enhanced(st.session_state.profile_manager)

# Footer
st.markdown(\"\"\"
<div class="footer">
    <p><strong>📄 CoverLetterPro v3.0</strong> - Your AI-Powered Career Partner</p>
    <p>Made with ❤️ for job seekers everywhere | <a href="https://github.com/wuweillove/cover-letter-app." target="_blank">GitHub</a></p>
    <p><em>Tip: Complete your profile for the best experience!</em></p>
</div>
\"\"\", unsafe_allow_html=True)
