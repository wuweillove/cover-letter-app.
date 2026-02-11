import streamlit as st

class ThemeManager:
    """Manages light/dark theme switching and custom styling."""
    
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
                'secondary': '#764ba2',
                'background': '#ffffff',
                'surface': '#f8f9fa',
                'text': '#2c3e50',
                'text_secondary': '#7f8c8d',
                'border': '#e0e0e0',
                'success': '#10b981',
                'warning': '#f59e0b',
                'error': '#ef4444',
                'info': '#3b82f6'
            }
        else:
            return {
                'primary': '#8b5cf6',
                'secondary': '#ec4899',
                'background': '#1a1a2e',
                'surface': '#16213e',
                'text': '#eaeaea',
                'text_secondary': '#a0a0a0',
                'border': '#2d3748',
                'success': '#10b981',
                'warning': '#f59e0b',
                'error': '#ef4444',
                'info': '#3b82f6'
            }

def apply_custom_css(theme):
    """Apply custom CSS based on current theme."""
    tm = ThemeManager()
    colors = tm.get_theme_colors()
    
    css = f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* Main Header */
    .main-header {{
        background: linear-gradient(135deg, {colors['primary']} 0%, {colors['secondary']} 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        animation: fadeInDown 0.6s ease-out;
    }}
    
    .main-header h1 {{
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }}
    
    .main-header .subtitle {{
        font-size: 1.2rem;
        margin: 0.5rem 0;
        font-weight: 500;
    }}
    
    .main-header .tagline {{
        font-size: 0.95rem;
        opacity: 0.95;
        margin: 0.5rem 0 0 0;
    }}
    
    /* Progress Container */
    .progress-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 1.5rem 0;
        padding: 1rem;
        background: {colors['surface']};
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}
    
    .progress-step {{
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
        padding: 0.5rem;
        font-size: 0.85rem;
        font-weight: 500;
        color: {colors['text_secondary']};
        transition: all 0.3s ease;
    }}
    
    .progress-step.active {{
        color: {colors['primary']};
        font-weight: 600;
        transform: scale(1.05);
    }}
    
    .progress-step.completed {{
        color: {colors['success']};
    }}
    
    /* Score Cards */
    .score-card {{
        background: {colors['surface']};
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid {colors['border']};
    }}
    
    .score-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }}
    
    .score-value {{
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    
    .score-label {{
        font-size: 0.9rem;
        color: {colors['text_secondary']};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    /* Keyword Badges */
    .keyword-badge {{
        display: inline-block;
        padding: 0.4rem 0.9rem;
        margin: 0.3rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    .keyword-badge.matched {{
        background: linear-gradient(135deg, {colors['success']} 0%, #059669 100%);
        color: white;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
    }}
    
    .keyword-badge.missing {{
        background: {colors['surface']};
        color: {colors['text_secondary']};
        border: 2px dashed {colors['warning']};
    }}
    
    .keyword-badge:hover {{
        transform: scale(1.05);
    }}
    
    /* Buttons */
    .stButton>button {{
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }}
    
    /* Text Areas */
    .stTextArea textarea {{
        border-radius: 8px;
        border: 2px solid {colors['border']};
        transition: border-color 0.3s ease;
    }}
    
    .stTextArea textarea:focus {{
        border-color: {colors['primary']};
        box-shadow: 0 0 0 3px {colors['primary']}33;
    }}
    
    /* Expanders */
    .streamlit-expanderHeader {{
        background: {colors['surface']};
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    
    .streamlit-expanderHeader:hover {{
        background: {colors['primary']}22;
    }}
    
    /* Footer */
    .footer {{
        margin-top: 3rem;
        padding: 2rem;
        background: {colors['surface']};
        border-radius: 10px;
        text-align: center;
        color: {colors['text_secondary']};
    }}
    
    .footer a {{
        color: {colors['primary']};
        text-decoration: none;
        font-weight: 500;
    }}
    
    .footer a:hover {{
        text-decoration: underline;
    }}
    
    /* Animations */
    @keyframes fadeInDown {{
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
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    /* Metrics */
    .stMetric {{
        background: {colors['surface']};
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid {colors['primary']};
    }}
    
    /* Info boxes */
    .stAlert {{
        border-radius: 8px;
        animation: fadeIn 0.5s ease-out;
    }}
    
    /* Sidebar */
    .css-1d391kg {{
        background: {colors['surface']};
    }}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 10px;
        height: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {colors['surface']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {colors['primary']};
        border-radius: 5px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {colors['secondary']};
    }}
    
    /* Loading spinner */
    .stSpinner > div {{
        border-top-color: {colors['primary']} !important;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
