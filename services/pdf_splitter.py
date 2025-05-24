from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
from services.base_service import BaseService

class PDFSplitterService(BaseService):
    """Service for PDF splitting operations"""
    
    def get_page_count(self, uploaded_file):
        """Get the total number of pages in PDF"""
        pdf_reader = PdfReader(BytesIO(uploaded_file.getvalue()))
        return len(pdf_reader.pages)
    
    def split_pdf(self, uploaded_file, start_page, end_page):
        """Split PDF and return the result"""
        pdf_reader = PdfReader(BytesIO(uploaded_file.getvalue()))
        pdf_writer = PdfWriter()
        
        for page_num in range(start_page - 1, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_buffer = BytesIO()
        pdf_writer.write(output_buffer)
        output_buffer.seek(0)
        
        return output_buffer.getvalue()