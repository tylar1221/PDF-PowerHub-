import tempfile
import os
from abc import ABC, abstractmethod

class BaseService(ABC):
    """Base service class with common functionality"""
    
    def create_temp_file(self, suffix=''):
        """Create a temporary file and return its path"""
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        return temp_file.name
    
    def cleanup_temp_file(self, file_path):
        """Clean up temporary file"""
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
        except Exception:
            pass  # Ignore cleanup errors
    
    def write_uploaded_file_to_temp(self, uploaded_file, suffix=''):
        """Write uploaded file to temporary location"""
        temp_path = self.create_temp_file(suffix)
        with open(temp_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
        return temp_path
