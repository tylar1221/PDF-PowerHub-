import streamlit as st
from config.app_config import AppConfig

class UILayout:
    """✨ Handles all UI layout and rendering for PDF PowerHub ✨"""
    
    def __init__(self):
        """Initialize UI Layout with theme management"""
        self._init_theme()
    
    def _init_theme(self):
        """Initialize theme state"""
        if 'dark_mode' not in st.session_state:
            st.session_state.dark_mode = False
    
    def _get_theme_colors(self):
        """Get theme-specific colors"""
        if st.session_state.dark_mode:
            return {
                'bg_primary': '#0e1117',
                'bg_secondary': '#262730',
                'bg_tertiary': '#1e1e1e',
                'text_primary': '#ffffff',
                'text_secondary': '#b3b3b3',
                'accent': '#ff6b6b',
                'success': '#4caf50',
                'info': '#2196f3',
                'warning': '#ff9800',
                'border': '#404040',
                'card_bg': '#1a1a1a',
                'hover_bg': '#333333'
            }
        else:
            return {
                'bg_primary': '#ffffff',
                'bg_secondary': '#f0f2f6',
                'bg_tertiary': '#fafafa',
                'text_primary': '#262730',
                'text_secondary': '#6c757d',
                'accent': '#1f77b4',
                'success': '#28a745',
                'info': '#17a2b8',
                'warning': '#ffc107',
                'border': '#dee2e6',
                'card_bg': '#ffffff',
                'hover_bg': '#f8f9fa'
            }
    
    def _apply_theme_css(self):
        """Apply theme-specific CSS"""
        colors = self._get_theme_colors()
        theme_name = "dark" if st.session_state.dark_mode else "light"
        
        st.markdown(f"""
        <style>
        /* Theme: {theme_name} */
        
        /* Main containers */
        .stApp {{
            background-color: {colors['bg_primary']};
            color: {colors['text_primary']};
        }}
        
        /* Sidebar styling */
        .css-1d391kg {{
            background-color: {colors['bg_secondary']};
        }}
        
        .css-1v0mbdj {{
            background-color: {colors['bg_secondary']};
        }}
        
        /* Feature cards */
        .feature-card {{
            background: {colors['card_bg']};
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid {colors['border']};
            margin: 1rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }}
        
        .feature-card:hover {{
            background: {colors['hover_bg']};
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }}
        
        .feature-card h3 {{
            color: {colors['accent']};
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
        }}
        
        .feature-card ul {{
            list-style: none;
            padding: 0;
        }}
        
        .feature-card li {{
            color: {colors['text_secondary']};
            margin: 0.5rem 0;
            padding-left: 1rem;
            position: relative;
        }}
        
        .feature-card li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: {colors['success']};
            font-weight: bold;
        }}
        
        /* Main header */
        .main-header {{
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, {colors['accent']}, {colors['info']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }}
        
        /* Step cards */
        .step-card {{
            background: {colors['bg_tertiary']};
            padding: 1rem;
            border-left: 4px solid {colors['accent']};
            margin: 0.5rem 0;
            border-radius: 0 8px 8px 0;
        }}
        
        /* Theme toggle */
        .theme-toggle {{
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 999;
            background: {colors['card_bg']};
            border: 1px solid {colors['border']};
            border-radius: 50px;
            padding: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        /* Success/Info boxes */
        .success-box {{
            background-color: {colors['success']}20;
            border: 1px solid {colors['success']};
            color: {colors['success']};
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }}
        
        .info-box {{
            background-color: {colors['info']}20;
            border: 1px solid {colors['info']};
            color: {colors['info']};
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }}
        
        .warning-box {{
            background-color: {colors['warning']}20;
            border: 1px solid {colors['warning']};
            color: {colors['warning']};
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }}
        
        /* File uploader styling */
        .uploadedFile {{
            background-color: {colors['card_bg']} !important;
            border: 2px dashed {colors['border']} !important;
            border-radius: 8px !important;
        }}
        
        /* Button styling */
        .stButton > button {{
            background: linear-gradient(45deg, {colors['accent']}, {colors['info']});
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        }}
        
        /* Download button styling */
        .stDownloadButton > button {{
            background: linear-gradient(45deg, {colors['success']}, #45a049);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }}
        
        /* Selectbox and input styling */
        .stSelectbox > div > div {{
            background-color: {colors['card_bg']};
            border: 1px solid {colors['border']};
            color: {colors['text_primary']};
        }}
        
        .stNumberInput > div > div > input {{
            background-color: {colors['card_bg']};
            border: 1px solid {colors['border']};
            color: {colors['text_primary']};
        }}
        
        /* Progress bar */
        .stProgress > div > div {{
            background: linear-gradient(45deg, {colors['accent']}, {colors['success']});
        }}
        </style>
        """, unsafe_allow_html=True)
    
    def render_theme_toggle(self):
        """Render theme toggle button in sidebar"""
        st.sidebar.markdown("---")
        
        theme_icon = "🌙" if not st.session_state.dark_mode else "☀️"
        theme_text = "Dark Mode" if not st.session_state.dark_mode else "Light Mode"
        
        if st.sidebar.button(f"{theme_icon} {theme_text}", key="theme_toggle"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    
    def render_header(self):
        """Render the stylish main header"""
        self._apply_theme_css()
        
        st.markdown(f'''
        <div class="main-header">
            {AppConfig.APP_ICON} {AppConfig.APP_TITLE}
        </div>
        ''', unsafe_allow_html=True)
        
        st.caption("📄 A smart, sleek tool to handle all your PDF needs.")
    
    def render_sidebar(self):
        """Render sidebar with navigation and theme toggle"""
        st.sidebar.title("📚 PDF PowerHub")
        st.sidebar.markdown("🚀 **What would you like to do today?**")
        
        operation = st.sidebar.radio(
            "Choose an action:",
            list(AppConfig.OPERATIONS.values())
        )
        
        # Add theme toggle at the bottom of sidebar
        self.render_theme_toggle()
        
        return operation
    
    def render_home_page(self):
        """Render homepage content with theme support"""
        st.header("👋 Welcome to PDF PowerHub!")
        st.write("Your all-in-one solution to edit, convert, and manage PDF files with ease.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            self._render_feature_section("🔁 Convert PDF", [
                "➡️ PDF to Word (.docx)",
                "🖼️ PDF to PNG images", 
                "🔤 PDF to Text"
            ])
            self._render_feature_section("➕ Merge PDFs", [
                "🧩 Combine multiple PDFs into one",
                "📐 Maintain original layout and quality",
                "🔢 Custom page ordering"
            ])
        
        with col2:
            self._render_feature_section("✂️ Split PDF", [
                "📄 Extract specific page ranges",
                "📂 Create smaller, separate files",
                "🎯 Flexible page selection"
            ])
            self._render_feature_section("🗜️ Compress PDF", [
                "🔽 Reduce file size",
                "👁️ Maintain readability", 
                "📤 Optimize for sharing"
            ])
        
        st.divider()
        
        st.subheader("🛠️ Getting Started is Easy")
        steps = [
            "👉 **Step 1:** Pick an operation from the sidebar",
            "📤 **Step 2:** Upload your PDF file(s)",
            "⚙️ **Step 3:** Customize your settings",
            "📥 **Step 4:** Download your optimized file!"
        ]
        
        for i, step in enumerate(steps, 1):
            st.markdown(f'''
            <div class="step-card">
                {step}
            </div>
            ''', unsafe_allow_html=True)
    
    def _render_feature_section(self, title, features):
        """Display a feature section with enhanced styling"""
        features_html = "".join([f"<li>{feature}</li>" for feature in features])
        
        st.markdown(f'''
        <div class="feature-card">
            <h3>{title}</h3>
            <ul>
                {features_html}
            </ul>
        </div>
        ''', unsafe_allow_html=True)
    
    def render_file_uploader(self, label, file_types, multiple=False, help_text=None):
        """Fancy file uploader with theme support"""
        return st.file_uploader(
            label=label,
            type=file_types,
            accept_multiple_files=multiple,
            help=help_text
        )
    
    def render_download_button(self, label, data, filename, mime_type):
        """Polished download button with theme support"""
        return st.download_button(
            label=f"📥 {label}",
            data=data,
            file_name=filename,
            mime=mime_type
        )
    
    def render_success_message(self, message):
        """Render themed success message"""
        st.markdown(f'''
        <div class="success-box">
            ✅ {message}
        </div>
        ''', unsafe_allow_html=True)
    
    def render_info_message(self, message):
        """Render themed info message"""
        st.markdown(f'''
        <div class="info-box">
            ℹ️ {message}
        </div>
        ''', unsafe_allow_html=True)
    
    def render_warning_message(self, message):
        """Render themed warning message"""
        st.markdown(f'''
        <div class="warning-box">
            ⚠️ {message}
        </div>
        ''', unsafe_allow_html=True)
    
    def render_progress_bar(self, progress, text="Processing..."):
        """Render themed progress bar"""
        progress_bar = st.progress(progress)
        st.text(text)
        return progress_bar