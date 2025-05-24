import streamlit as st

class SessionManager:
    """Manages Streamlit session state"""
    
    @staticmethod
    def initialize():
        """Initialize session state variables"""
        if 'initialized' not in st.session_state:
            st.session_state.initialized = True
            st.session_state.operation_history = []
    
    @staticmethod
    def add_to_history(operation, details):
        """Add operation to history"""
        if 'operation_history' not in st.session_state:
            st.session_state.operation_history = []
        
        st.session_state.operation_history.append({
            'operation': operation,
            'details': details,
            'timestamp': st.session_state.get('timestamp', 'N/A')
        })
    
    @staticmethod
    def get_history():
        """Get operation history"""
        return st.session_state.get('operation_history', [])
    
    @staticmethod
    def clear_history():
        """Clear operation history"""
        st.session_state.operation_history = []
