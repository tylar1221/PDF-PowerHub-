import PyPDF2
from io import BytesIO
from services.base_service import BaseService

class PDFMergerService(BaseService):
    """Service for PDF merging operations"""
    
    def merge_pdfs(self, uploaded_files):
        """Merge multiple PDFs into one"""
        pdf_merger = PyPDF2.PdfMerger()
        
        try:
            for uploaded_file in uploaded_files:
                pdf_merger.append(BytesIO(uploaded_file.getvalue()))
            
            output_buffer = BytesIO()
            pdf_merger.write(output_buffer)
            output_buffer.seek(0)
            
            return output_buffer.getvalue()
        finally:
            pdf_merger.close()
