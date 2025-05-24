# PDF PowerHub 📘

A comprehensive PDF management and conversion tool built with Streamlit. Transform, split, merge, and compress your PDF files with ease through an intuitive web interface.

## ✨ Features

### 🔁 PDF Conversion
- **PDF to Word (.docx)** - Convert PDF documents to editable Word format
- **PDF to PNG Images** - Extract pages as high-quality PNG images
- **PDF to Text** - Extract text content from PDF documents

### ✂️ PDF Splitting
- Extract specific page ranges from PDF documents
- Create multiple smaller files from large PDFs
- Flexible page selection with preview

### ➕ PDF Merging
- Combine multiple PDF files into a single document
- Maintain original quality and formatting
- Custom file ordering support

### 🗜️ PDF Compression
- Reduce file size while maintaining readability
- Multiple compression levels (Low, Medium, High)
- Real-time size reduction metrics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pdf-powerhub.git
   cd pdf-powerhub
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🏗️ Project Structure

```
pdf-powerhub/
├── main.py                    # Application entry point
├── config/
│   └── app_config.py         # Configuration settings
├── ui/
│   └── layout.py             # UI components and layouts
├── controllers/
│   └── pdf_controller.py     # Main application logic
├── services/
│   ├── base_service.py       # Base service class
│   ├── pdf_converter.py     # PDF conversion services
│   ├── pdf_splitter.py      # PDF splitting services
│   ├── pdf_merger.py        # PDF merging services
│   └── pdf_compressor.py    # PDF compression services
├── utils/
│   ├── session_manager.py   # Session state management
│   ├── file_validator.py    # File validation utilities
│   └── error_handler.py     # Error handling utilities
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit - Modern web app framework for Python
- **PDF Processing**: 
  - PyPDF2 - PDF manipulation and merging
  - PyMuPDF (fitz) - PDF compression and advanced operations
  - pdf2image - PDF to image conversion
  - pdf2docx - PDF to Word conversion
  - pdfminer.six - Text extraction
- **Image Processing**: Pillow - Image manipulation and format conversion

## 📋 Requirements

```txt
streamlit>=1.28.0
PyPDF2>=3.0.0
pdf2image>=1.16.0
pdf2docx>=0.5.6
PyMuPDF>=1.23.0
pdfminer.six>=20221105
Pillow>=9.0.0
```

## 🎯 Usage Examples

### Converting PDF to Word
1. Select "Convert PDF" from the sidebar
2. Upload your PDF file
3. Choose "PDF to Word (.docx)" from the conversion options
4. Click "Convert File" and download the result

### Splitting a PDF
1. Select "Split PDF" from the sidebar
2. Upload your PDF file
3. Specify the page range (start and end pages)
4. Click "Split PDF" and download the extracted pages

### Merging Multiple PDFs
1. Select "Merge PDFs" from the sidebar
2. Upload multiple PDF files
3. Review the file order
4. Click "Merge PDFs" and download the combined document

### Compressing a PDF
1. Select "Compress PDF" from the sidebar
2. Upload your PDF file
3. Choose compression level (Low/Medium/High)
4. Click "Compress PDF" and download the optimized file

## 🔧 Configuration

The application can be configured through `config/app_config.py`:

- **Compression Levels**: Adjust quality and DPI settings
- **Supported Formats**: Modify accepted file types
- **UI Settings**: Customize app title, icon, and layout

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add appropriate error handling
- Include docstrings for new functions
- Test your changes thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues and Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/pdf-powerhub/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🚀 Deployment

### Local Development
```bash
streamlit run main.py
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Streamlit Cloud
1. Fork this repository
2. Connect your GitHub account to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy directly from your repository

## 📊 Performance Notes

- Large PDF files may take longer to process
- Image conversion requires sufficient memory
- Compression results vary based on PDF content
- Processing time scales with file size and complexity

## 🔒 Security Considerations

- Files are processed locally and temporarily
- No data is stored permanently on the server
- Temporary files are automatically cleaned up
- Consider file size limits for production deployment

## 📈 Future Enhancements

- [ ] Password-protected PDF support
- [ ] Batch processing capabilities
- [ ] OCR text extraction
- [ ] PDF metadata editing
- [ ] Custom compression algorithms
- [ ] API endpoint support
- [ ] Multiple language support

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- PyPDF2 contributors for PDF manipulation tools
- All open-source libraries that make this project possible

---

**Made with ❤️ and Python**
