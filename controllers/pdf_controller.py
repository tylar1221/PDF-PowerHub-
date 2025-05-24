import streamlit as st
from config.app_config import AppConfig
from ui.layout import UILayout
from services.pdf_converter import PDFConverterService
from services.pdf_splitter import PDFSplitterService
from services.pdf_merger import PDFMergerService
from services.pdf_compressor import PDFCompressorService

class PDFController:
    """Main controller for handling PDF operations"""
    
    def __init__(self):
        self.ui = UILayout()
        self.converter_service = PDFConverterService()
        self.splitter_service = PDFSplitterService()
        self.merger_service = PDFMergerService()
        self.compressor_service = PDFCompressorService()
    
    def handle_operation(self, operation):
        """Route operations to appropriate handlers"""
        operation_map = {
            AppConfig.OPERATIONS["home"]: self._handle_home,
            AppConfig.OPERATIONS["convert"]: self._handle_convert,
            AppConfig.OPERATIONS["split"]: self._handle_split,
            AppConfig.OPERATIONS["merge"]: self._handle_merge,
            AppConfig.OPERATIONS["compress"]: self._handle_compress
        }
        
        handler = operation_map.get(operation)
        if handler:
            handler()
        else:
            st.error(f"Unknown operation: {operation}")
    
    def _handle_home(self):
        """Handle home page display"""
        self.ui.render_home_page()
    
    def _handle_convert(self):
        """Handle PDF conversion operations"""
        st.header("🔁 Convert PDF")
        
        uploaded_file = self.ui.render_file_uploader(
            "Upload a PDF file", 
            AppConfig.SUPPORTED_FORMATS["pdf"]
        )
        
        if uploaded_file is not None:
            conversion_type = st.selectbox(
                "Choose conversion type:",
                ["PDF to Word (.docx)", "PDF to PNG Images", "PDF to Text"]
            )
            
            if st.button("Convert File", type="primary"):
                with st.spinner("Converting your file..."):
                    try:
                        result = self.converter_service.convert(
                            uploaded_file, conversion_type
                        )
                        self._handle_conversion_result(result, uploaded_file.name)
                    except Exception as e:
                        st.error(f"Conversion failed: {str(e)}")
    
    def _handle_split(self):
        """Handle PDF splitting operations"""
        st.header("✂️ Split PDF")
        
        uploaded_file = self.ui.render_file_uploader(
            "Upload a PDF file to split",
            AppConfig.SUPPORTED_FORMATS["pdf"]
        )
        
        if uploaded_file is not None:
            total_pages = self.splitter_service.get_page_count(uploaded_file)
            st.info(f"Total pages in PDF: {total_pages}")
            
            col1, col2 = st.columns(2)
            with col1:
                start_page = st.number_input("Start page", min_value=1, max_value=total_pages, value=1)
            with col2:
                end_page = st.number_input("End page", min_value=start_page, max_value=total_pages, value=total_pages)
            
            if st.button("Split PDF", type="primary"):
                try:
                    result = self.splitter_service.split_pdf(uploaded_file, start_page, end_page)
                    st.success(f"PDF split successfully! Pages {start_page}-{end_page}")
                    
                    filename = f"{uploaded_file.name.replace('.pdf', '')}_pages_{start_page}-{end_page}.pdf"
                    self.ui.render_download_button(
                        "Download Split PDF", result, filename, "application/pdf"
                    )
                except Exception as e:
                    st.error(f"Split failed: {str(e)}")
    
    def _handle_merge(self):
        """Handle PDF merging operations"""
        st.header("➕ Merge PDFs")
        
        uploaded_files = self.ui.render_file_uploader(
            "Upload PDF files to merge",
            AppConfig.SUPPORTED_FORMATS["pdf"],
            multiple=True,
            help_text="You can upload multiple files at once"
        )
        
        if uploaded_files:
            st.info(f"{len(uploaded_files)} PDF files uploaded")
            
            st.write("**File Order:**")
            for i, file in enumerate(uploaded_files):
                st.write(f"{i+1}. {file.name}")
            
            if len(uploaded_files) > 1:
                if st.button("Merge PDFs", type="primary"):
                    try:
                        with st.spinner("Merging PDFs..."):
                            result = self.merger_service.merge_pdfs(uploaded_files)
                            st.success(f"{len(uploaded_files)} PDFs merged successfully!")
                            
                            self.ui.render_download_button(
                                "Download Merged PDF", result, "merged_document.pdf", "application/pdf"
                            )
                    except Exception as e:
                        st.error(f"Merge failed: {str(e)}")
            else:
                st.warning("Please upload at least 2 PDF files to merge.")
    
    def _handle_compress(self):
        """Handle PDF compression operations"""
        st.header("🗜️ Compress PDF")
        
        uploaded_file = self.ui.render_file_uploader(
            "Upload a PDF file to compress",
            AppConfig.SUPPORTED_FORMATS["pdf"]
        )
        
        if uploaded_file is not None:
            original_size = len(uploaded_file.getvalue()) / 1024
            st.info(f"Original file size: {original_size:.2f} KB")
            
            compression_level = st.select_slider(
                "Compression Level:",
                options=list(AppConfig.COMPRESSION_LEVELS.keys()),
                value="Medium",
                help="Higher compression = smaller file size but potentially lower quality"
            )
            
            if st.button("Compress PDF", type="primary"):
                with st.spinner("Compressing PDF..."):
                    try:
                        result = self.compressor_service.compress_pdf(uploaded_file, compression_level)
                        compressed_size = len(result) / 1024
                        reduction = ((original_size - compressed_size) / original_size) * 100
                        
                        st.success("PDF compressed successfully!")
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Original Size", f"{original_size:.2f} KB")
                        with col2:
                            st.metric("New Size", f"{compressed_size:.2f} KB")
                        with col3:
                            st.metric("Reduction", f"{reduction:.1f}%")
                        
                        filename = f"{uploaded_file.name.replace('.pdf', '')}_compressed.pdf"
                        self.ui.render_download_button(
                            "Download Compressed PDF", result, filename, "application/pdf"
                        )
                    except Exception as e:
                        st.error(f"Compression failed: {str(e)}")
    
    def _handle_conversion_result(self, result, original_filename):
        """Handle the result of PDF conversion"""
        if result["type"] == "single_file":
            st.success(result["message"])
            self.ui.render_download_button(
                result["button_label"],
                result["data"],
                result["filename"],
                result["mime_type"]
            )
        elif result["type"] == "text_preview":
            st.success(result["message"])
            with st.expander("View Extracted Text"):
                st.text_area("Content:", value=result["text"], height=300, disabled=True)
            self.ui.render_download_button(
                result["button_label"],
                result["data"],
                result["filename"],
                result["mime_type"]
            )
        elif result["type"] == "multiple_files":
            st.success(result["message"])
            self.ui.render_download_button(
                result["button_label"],
                result["data"],
                result["filename"],
                result["mime_type"]
            )
