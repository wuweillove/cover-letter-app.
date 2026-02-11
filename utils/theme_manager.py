import streamlit as st

class ThemeManager:
    """Enhanced Theme Manager with modern design system."""
    
    def __init__(self):
        if 'theme' not in st.session_state:
            st.session_state.theme = 'light'
    
    def get_current_theme(self):
        return st.session_state.theme
    
    def toggle_theme(self):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
    
    def get_theme_colors(self):
        if st.session_state.theme == 'light':
            return {
                'primary': '#667eea',
                'primary_dark': '#5568d3',
                'secondary': '#764ba2',
                'accent': '#f093fb',
                'background': '#f5f7fa',
                'surface': '#ffffff',
                'card': '#ffffff',
                'text': '#2d3748',
                'text_secondary': '#718096',
                'text_muted': '#a0aec0',
                'border': '#e2e8f0',
                'success': '#48bb78',
                'warning': '#ed8936',
                'error': '#e53e3e',
                'info': '#4299e1',
                'gradient_start': '#667eea',
                'gradient_end': '#764ba2'
            }
        else:
            return {
                'primary': '#8b5cf6',
                'primary_dark': '#7c3aed',
                'secondary': '#ec4899',
                'accent': '#f0abfc',
                'background': '#1a202c',
                'surface': '#2d3748',
                'card': '#2d3748',
                'text': '#f7fafc',
                'text_secondary': '#cbd5e0',
                'text_muted': '#a0aec0',
                'border': '#4a5568',
                'success': '#48bb78',
                'warning': '#ed8936',
                'error': '#e53e3e',
                'info': '#4299e1',
                'gradient_start': '#8b5cf6',
                'gradient_end': '#ec4899'
            }

def apply_custom_css(theme):
    """Apply modern custom CSS based on current theme."""
    tm = ThemeManager()
    colors = tm.get_theme_colors()
    
    css = f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }}
    
    /* Main App Container */
    .main .block-container {{
        padding-top: 1rem;
        background: {colors['background']};
    }}
    
    /* Modern Profile Header */
    .profile-header {{
        background: linear-gradient(135deg, {colors['gradient_start']} 0%, {colors['gradient_end']} 100%);
        color: white;
        padding: 2rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        animation: slideDown 0.5s ease-out;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1.5rem;
    }}
    
    .profile-header-left {{
        display: flex;
        align-items: center;
        gap: 1.5rem;
        flex: 1;
    }}
    
    .profile-avatar {{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 700;
        color: {colors['primary']};
        border: 4px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        overflow: hidden;
    }}
    
    .profile-avatar img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    
    .profile-info h1 {{
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    .profile-info p {{
        margin: 0.3rem 0 0 0;
        opacity: 0.95;
        font-size: 1.1rem;
        font-weight: 500;
    }}
    
    .profile-completion {{
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        border: 2px solid rgba(255,255,255,0.3);
    }}
    
    .profile-completion-label {{
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
        opacity: 0.9;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .profile-completion-value {{
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }}
    
    /* Main Header */
    .main-header {{
        background: linear-gradient(135deg, {colors['gradient_start']} 0%, {colors['gradient_end']} 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        animation: fadeInDown 0.6s ease-out;
    }}
    
    .main-header h1 {{
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        letter-spacing: -0.5px;
    }}
    
    .main-header .subtitle {{
        font-size: 1.3rem;
        margin: 0.8rem 0;
        font-weight: 600;
        opacity: 0.95;
    }}
    
    .main-header .tagline {{
        font-size: 1rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
        font-weight: 400;
    }}
    
    /* Modern Cards */
    .modern-card {{
        background: {colors['card']};
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid {colors['border']};
        transition: all 0.3s ease;
        animation: fadeIn 0.5s ease-out;
    }}
    
    .modern-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }}
    
    .card-header {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid {colors['border']};
    }}
    
    .card-header-icon {{
        font-size: 1.5rem;
    }}
    
    .card-header h3 {{
        margin: 0;
        color: {colors['text']};
        font-size: 1.3rem;
        font-weight: 700;
    }}
    
    /* Progress Container */
    .progress-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 1.5rem 0;
        padding: 1.5rem;
        background: {colors['surface']};
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1px solid {colors['border']};
    }}
    
    .progress-step {{
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
        padding: 0.75rem;
        font-size: 0.9rem;
        font-weight: 600;
        color: {colors['text_secondary']};
        transition: all 0.3s ease;
        border-radius: 8px;
    }}
    
    .progress-step.active {{
        color: white;
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        transform: scale(1.08);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }}
    
    .progress-step.completed {{
        color: {colors['success']};
        background: rgba(72, 187, 120, 0.1);
    }}
    
    /* Score Cards */
    .score-card {{
        background: linear-gradient(135deg, {colors['surface']} 0%, {colors['card']} 100%);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 2px solid {colors['border']};
        position: relative;
        overflow: hidden;
    }}
    
    .score-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {colors['primary']} 0%, {colors['secondary']} 100%);
    }}
    
    .score-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        border-color: {colors['primary']};
    }}
    
    .score-value {{
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .score-label {{
        font-size: 0.9rem;
        color: {colors['text_secondary']};
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    /* Keyword Badges */
    .keyword-badge {{
        display: inline-block;
        padding: 0.5rem 1.2rem;
        margin: 0.4rem;
        border-radius: 25px;
        font-size: 0.875rem;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: default;
    }}
    
    .keyword-badge.matched {{
        background: linear-gradient(135deg, {colors['success']} 0%, #059669 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(72, 187, 120, 0.3);
    }}
    
    .keyword-badge.matched:hover {{
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 6px 20px rgba(72, 187, 120, 0.4);
    }}
    
    .keyword-badge.missing {{
        background: {colors['surface']};
        color: {colors['text_secondary']};
        border: 2px dashed {colors['warning']};
    }}
    
    .keyword-badge.missing:hover {{
        background: rgba(237, 137, 54, 0.1);
        transform: scale(1.05);
    }}
    
    /* Skill Badges */
    .skill-badge {{
        display: inline-block;
        padding: 0.6rem 1.3rem;
        margin: 0.4rem;
        background: linear-gradient(135deg, rgba({colors['primary'][1:]}, 0.1) 0%, rgba({colors['secondary'][1:]}, 0.1) 100%);
        color: {colors['primary']};
        border-radius: 30px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 2px solid {colors['primary']}33;
        transition: all 0.3s ease;
    }}
    
    .skill-badge:hover {{
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(102, 126, 234, 0.3);
    }}
    
    /* Buttons */
    .stButton>button {{
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }}
    
    .stButton>button:active {{
        transform: translateY(-1px);
    }}
    
    /* Primary Button */
    .stButton>button[kind="primary"] {{
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        color: white;
    }}
    
    .stButton>button[kind="primary"]:hover {{
        background: linear-gradient(135deg, {colors['primary_dark']} 0%, {colors['secondary']} 100%);
    }}
    
    /* Text Input & Text Area */
    .stTextInput>div>div>input,
    .stTextArea textarea {{
        border-radius: 12px;
        border: 2px solid {colors['border']};
        transition: all 0.3s ease;
        font-size: 1rem;
        padding: 0.75rem;
        background: {colors['surface']};
        color: {colors['text']};
    }}
    
    .stTextInput>div>div>input:focus,
    .stTextArea textarea:focus {{
        border-color: {colors['primary']};
        box-shadow: 0 0 0 4px {colors['primary']}22;
        outline: none;
    }}
    
    /* Select Boxes */
    .stSelectbox>div>div>div {{
        border-radius: 12px;
        border: 2px solid {colors['border']};
        background: {colors['surface']};
    }}
    
    /* Expanders */
    .streamlit-expanderHeader {{
        background: {colors['surface']};
        border-radius: 12px;
        font-weight: 600;
        padding: 1rem;
        transition: all 0.3s ease;
        border: 2px solid {colors['border']};
        color: {colors['text']};
    }}
    
    .streamlit-expanderHeader:hover {{
        background: linear-gradient(135deg, {colors['primary']}11 0%, {colors['secondary']}11 100%);
        border-color: {colors['primary']};
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: {colors['surface']};
        padding: 0.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        background: {colors['primary']}11;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        color: white !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }}
    
    /* Metrics */
    .stMetric {{
        background: {colors['surface']};
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid {colors['primary']};
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }}
    
    .stMetric:hover {{
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    .stMetric label {{
        color: {colors['text_secondary']} !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }}
    
    .stMetric .metric-value {{
        color: {colors['text']} !important;
        font-weight: 700 !important;
    }}
    
    /* Info/Alert Boxes */
    .stAlert {{
        border-radius: 12px;
        animation: fadeIn 0.5s ease-out;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}
    
    /* Success Message */
    .stSuccess {{
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.1) 0%, rgba(72, 187, 120, 0.05) 100%);
        border-left: 4px solid {colors['success']};
    }}
    
    /* Warning Message */
    .stWarning {{
        background: linear-gradient(135deg, rgba(237, 137, 54, 0.1) 0%, rgba(237, 137, 54, 0.05) 100%);
        border-left: 4px solid {colors['warning']};
    }}
    
    /* Error Message */
    .stError {{
        background: linear-gradient(135deg, rgba(229, 62, 62, 0.1) 0%, rgba(229, 62, 62, 0.05) 100%);
        border-left: 4px solid {colors['error']};
    }}
    
    /* Info Message */
    .stInfo {{
        background: linear-gradient(135deg, rgba(66, 153, 225, 0.1) 0%, rgba(66, 153, 225, 0.05) 100%);
        border-left: 4px solid {colors['info']};
    }}
    
    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: {colors['surface']};
        border-right: 1px solid {colors['border']};
    }}
    
    section[data-testid="stSidebar"] .stMarkdown {{
        color: {colors['text']};
    }}
    
    /* Progress Bar */
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        border-radius: 10px;
        height: 8px;
    }}
    
    /* Divider */
    hr {{
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, {colors['border']} 50%, transparent 100%);
    }}
    
    /* Footer */
    .footer {{
        margin-top: 4rem;
        padding: 2rem;
        background: {colors['surface']};
        border-radius: 16px;
        text-align: center;
        color: {colors['text_secondary']};
        border-top: 3px solid {colors['primary']};
    }}
    
    .footer a {{
        color: {colors['primary']};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}
    
    .footer a:hover {{
        color: {colors['secondary']};
        text-decoration: underline;
    }}
    
    /* Animations */
    @keyframes fadeInDown {{
        from {{
            opacity: 0;
            transform: translateY(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes slideDown {{
        from {{
            opacity: 0;
            transform: translateY(-20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: scale(0.95); }}
        to {{ opacity: 1; transform: scale(1); }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 10px;
        height: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {colors['surface']};
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(180deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(180deg, {colors['primary_dark']} 0%, {colors['secondary']} 100%);
    }}
    
    /* Loading spinner */
    .stSpinner > div {{
        border-top-color: {colors['primary']} !important;
    }}
    
    /* File Uploader */
    .stFileUploader {{
        border-radius: 12px;
    }}
    
    .stFileUploader>div>div {{
        border: 2px dashed {colors['border']};
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s ease;
    }}
    
    .stFileUploader>div>div:hover {{
        border-color: {colors['primary']};
        background: {colors['primary']}08;
    }}
    
    /* Form Elements */
    .stForm {{
        border: none;
        padding: 0;
    }}
    
    /* Download Button */
    .stDownloadButton>button {{
        background: {colors['success']};
        color: white;
    }}
    
    .stDownloadButton>button:hover {{
        background: #059669;
    }}
    
    /* Checkbox */
    .stCheckbox {{
        color: {colors['text']};
    }}
    
    /* Number Input */
    .stNumberInput>div>div>input {{
        border-radius: 12px;
        border: 2px solid {colors['border']};
        background: {colors['surface']};
    }}
    
    /* Slider */
    .stSlider>div>div>div>div {{
        background: {colors['primary']};
    }}
    
    /* Text color fix */
    p, span, div, label {{
        color: {colors['text']};
    }}
    
    /* Markdown headings */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
        color: {colors['text']};
        font-weight: 700;
    }}
    
    /* Profile Edit Section */
    .profile-edit-section {{
        background: {colors['card']};
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
    }}
    
    .section-title {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        color: {colors['text']};
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid {colors['border']};
    }}
    
    .section-icon {{
        font-size: 1.5rem;
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    /* Avatar Upload Section */
    .avatar-upload {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        padding: 2rem;
        background: {colors['surface']};
        border-radius: 16px;
        border: 2px dashed {colors['border']};
        transition: all 0.3s ease;
    }}
    
    .avatar-upload:hover {{
        border-color: {colors['primary']};
        background: {colors['primary']}08;
    }}
    
    .avatar-preview {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        border: 4px solid white;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        overflow: hidden;
    }}
    
    .avatar-preview img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    
    /* Social Links */
    .social-link {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 1rem 1.25rem;
        background: {colors['surface']};
        border-radius: 12px;
        text-decoration: none;
        color: {colors['text']};
        transition: all 0.3s ease;
        border: 2px solid {colors['border']};
        margin-bottom: 0.75rem;
    }}
    
    .social-link:hover {{
        background: linear-gradient(135deg, {colors['primary']}11 0%, {colors['secondary']}11 100%);
        border-color: {colors['primary']};
        transform: translateX(8px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    .social-icon {{
        font-size: 1.3rem;
        color: {colors['primary']};
    }}
    
    /* Stats Grid */
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }}
    
    .stat-card {{
        background: {colors['card']};
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 2px solid {colors['border']};
        transition: all 0.3s ease;
    }}
    
    .stat-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        border-color: {colors['primary']};
    }}
    
    .stat-value {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {colors['primary']};
        margin: 0;
    }}
    
    .stat-label {{
        font-size: 0.9rem;
        color: {colors['text_secondary']};
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.5rem;
    }}
    
    /* Action Cards */
    .action-card {{
        background: {colors['card']};
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        border: 2px solid {colors['border']};
    }}
    
    .action-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        border-color: {colors['primary']};
    }}
    
    /* Badge */
    .badge {{
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .badge-primary {{
        background: {colors['primary']};
        color: white;
    }}
    
    .badge-success {{
        background: {colors['success']};
        color: white;
    }}
    
    .badge-warning {{
        background: {colors['warning']};
        color: white;
    }}
    
    /* Responsive Design */
    @media (max-width: 768px) {{
        .main-header h1 {{
            font-size: 2rem;
        }}
        
        .profile-header {{
            flex-direction: column;
            text-align: center;
        }}
        
        .profile-avatar {{
            width: 100px;
            height: 100px;
        }}
        
        .progress-container {{
            flex-direction: column;
            gap: 0.5rem;
        }}
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
