# main.py
import streamlit as st
from config.app_config import AppConfig
from ui.layout import UILayout
from controllers.pdf_controller import PDFController
from utils.session_manager import SessionManager

def main():
    # Initialize app configuration
    AppConfig.setup_page()
    
    # Initialize session manager
    SessionManager.initialize()
    
    # Initialize UI layout
    ui = UILayout()
    
    # Initialize PDF controller
    pdf_controller = PDFController()
    
    # Render main UI
    ui.render_header()
    operation = ui.render_sidebar()
    
    # Route to appropriate controller method
    pdf_controller.handle_operation(operation)

if __name__ == "__main__":
    main()