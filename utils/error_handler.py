import streamlit as st
import logging

class ErrorHandler:
    """Centralized error handling"""
    
    @staticmethod
    def handle_pdf_error(error, operation="PDF operation"):
        """Handle PDF-related errors"""
        error_msg = str(error)
        logging.error(f"{operation} failed: {error_msg}")
        
        if "corrupted" in error_msg.lower():
            st.error("The PDF file appears to be corrupted. Please try with a different file.")
        elif "permission" in error_msg.lower():
            st.error("Permission denied. The PDF file may be password-protected.")
        elif "memory" in error_msg.lower():
            st.error("File too large. Please try with a smaller PDF file.")
        else:
            st.error(f"{operation} failed: {error_msg}")
    
    @staticmethod
    def handle_conversion_error(error, conversion_type):
        """Handle conversion-specific errors"""
        error_msg = str(error)
        logging.error(f"{conversion_type} conversion failed: {error_msg}")
        st.error(f"Conversion to {conversion_type} failed. Please check your PDF file and try again.")
