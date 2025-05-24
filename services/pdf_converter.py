import pdf2image
from pdf2docx import Converter
from pdfminer.high_level import extract_text
import zipfile
from io import BytesIO
from services.base_service import BaseService

class PDFConverterService(BaseService):
    """Service for PDF conversion operations"""
    
    def convert(self, uploaded_file, conversion_type):
        """Convert PDF based on conversion type"""
        conversion_map = {
            "PDF to Word (.docx)": self._convert_to_word,
            "PDF to PNG Images": self._convert_to_images,
            "PDF to Text": self._convert_to_text
        }
        
        converter = conversion_map.get(conversion_type)
        if converter:
            return converter(uploaded_file)
        else:
            raise ValueError(f"Unknown conversion type: {conversion_type}")
    
    def _convert_to_word(self, uploaded_file):
        """Convert PDF to Word document"""
        temp_input = self.write_uploaded_file_to_temp(uploaded_file, '.pdf')
        temp_output = self.create_temp_file('.docx')
        
        try:
            cv = Converter(temp_input)
            cv.convert(temp_output)
            cv.close()
            
            with open(temp_output, 'rb') as f:
                docx_data = f.read()
            
            return {
                "type": "single_file",
                "message": "PDF converted to Word successfully!",
                "data": docx_data,
                "filename": f"{uploaded_file.name.replace('.pdf', '')}.docx",
                "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "button_label": "Download Word File"
            }
        finally:
            self.cleanup_temp_file(temp_input)
            self.cleanup_temp_file(temp_output)
    
    def _convert_to_images(self, uploaded_file):
        """Convert PDF to PNG images"""
        temp_path = self.write_uploaded_file_to_temp(uploaded_file, '.pdf')
        
        try:
            images = pdf2image.convert_from_path(temp_path)
            
            if len(images) == 1:
                # Single image
                img_buffer = BytesIO()
                images[0].save(img_buffer, format='PNG')
                
                return {
                    "type": "single_file",
                    "message": "PDF converted to PNG successfully!",
                    "data": img_buffer.getvalue(),
                    "filename": f"{uploaded_file.name.replace('.pdf', '')}.png",
                    "mime_type": "image/png",
                    "button_label": "Download PNG Image"
                }
            else:
                # Multiple images - create ZIP
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for i, image in enumerate(images):
                        img_buffer = BytesIO()
                        image.save(img_buffer, format='PNG')
                        zip_file.writestr(f"page_{i+1}.png", img_buffer.getvalue())
                
                return {
                    "type": "multiple_files",
                    "message": f"PDF converted to {len(images)} PNG images successfully!",
                    "data": zip_buffer.getvalue(),
                    "filename": f"{uploaded_file.name.replace('.pdf', '')}_images.zip",
                    "mime_type": "application/zip",
                    "button_label": "Download Images (ZIP)"
                }
        finally:
            self.cleanup_temp_file(temp_path)
    
    def _convert_to_text(self, uploaded_file):
        """Convert PDF to text"""
        temp_path = self.write_uploaded_file_to_temp(uploaded_file, '.pdf')
        
        try:
            text = extract_text(temp_path)
            
            return {
                "type": "text_preview",
                "message": "PDF converted to text successfully!",
                "text": text,
                "data": text.encode('utf-8'),
                "filename": f"{uploaded_file.name.replace('.pdf', '')}.txt",
                "mime_type": "text/plain",
                "button_label": "Download Text File"
            }
        finally:
            self.cleanup_temp_file(temp_path)
            st.write(f"{i+1}. {file.name}")
            st.write("**File Order:**")