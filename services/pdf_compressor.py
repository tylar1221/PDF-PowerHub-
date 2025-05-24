import fitz  # PyMuPDF
from config.app_config import AppConfig
from services.base_service import BaseService

class PDFCompressorService(BaseService):
    """Service for PDF compression operations"""
    
    def compress_pdf(self, uploaded_file, compression_level):
        """Compress PDF file"""
        temp_input = self.write_uploaded_file_to_temp(uploaded_file, '.pdf')
        temp_output = self.create_temp_file('.pdf')
        
        try:
            # Get compression settings
            settings = AppConfig.COMPRESSION_LEVELS[compression_level]
            quality = settings["quality"]
            
            # Open PDF with PyMuPDF
            doc = fitz.open(temp_input)
            
            # Compress images in PDF
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                image_list = page.get_images()
                
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Save compressed image back to PDF
                    pix = fitz.Pixmap(image_bytes)
                    if pix.n - pix.alpha < 4:  # GRAY or RGB
                        compressed_img = pix.tobytes("jpeg", jpg_quality=quality)
                        doc._updateStream(xref, compressed_img)
                    pix = None
            
            # Save compressed PDF
            doc.save(temp_output, garbage=4, deflate=True)
            doc.close()
            
            # Read compressed data
            with open(temp_output, 'rb') as f:
                compressed_data = f.read()
            
            return compressed_data
        
        finally:
            self.cleanup_temp_file(temp_input)
            self.cleanup_temp_file(temp_output)
