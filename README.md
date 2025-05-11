# **chi resume scanner**  

This repository contains all the files for the **chi resume scanner**, an AI-powered application that analyzes tech resumes and identifies which technical roles they're best optimized for.

Below is a breakdown of the project:  

## **Project Overview**  

**Goal**: Create an AI-powered resume analyzer for tech roles  
**Algorithms/Techniques In Focus**: Zero-shot classification, document processing, web interface  

**Description**:  
This application uses advanced natural language processing to match resume content against over 60 technical job categories to provide instant feedback on career fit. It features a modern UI with visual feedback and supports multiple document formats.  

## **Features**  

- **AI-Powered Analysis**: Uses zero-shot classification to evaluate resumes against tech job categories  
- **Multi-Format Support**: Processes PDF, DOCX, and TXT resume formats  
- **OCR Capability**: Extracts text from scanned PDFs using image recognition  
- **Interactive UI**: Modern, responsive interface with visual feedback and animations  
- **Comprehensive Role Coverage**: Evaluates against 60+ technical roles across software development, data science, hardware engineering, and more  

## **Tech Stack**  

- **Backend**: Python, Flask  
- **AI/ML**: Hugging Face Transformers, PyTorch  
- **Document Processing**: pdfplumber, pytesseract, python-docx  
- **Frontend**: HTML, CSS, JavaScript  

## **How It Works**  

1. **Upload**: User uploads their resume in PDF, DOCX, or TXT format  
2. **Text Extraction**: The application extracts plain text from the document using specialized libraries for each format  
3. **AI Analysis**: The extracted text is processed by a zero-shot classification model (`facebook/bart-large-mnli`)  
4. **Role Matching**: The model evaluates the resume against predefined tech job categories  
5. **Results Display**: The application presents the top matching role along with a breakdown of all matches  

## **Job Categories**  

The system analyzes resumes against categories including:  

- **Software & Development**: Software Engineer, Frontend Developer, Backend Developer, etc.  
- **Data & AI/ML**: Data Scientist, Machine Learning Engineer, AI Research Scientist, etc.  
- **Cloud & Infrastructure**: Cloud Architect, Site Reliability Engineer, etc.  
- **Hardware & Embedded**: Hardware Engineer, Electrical Engineer, Robotics Engineer, etc.  
- **General Engineering**: Mechanical Engineer, Aerospace Engineer, etc.  
- **Project & Program Management**: Product Manager, Project Manager  
- **IT & Business Analysis**: IT Analyst, Business Analyst, Solutions Architect, etc.  
- **UX/UI & Design**: UI/UX Developer, Visual Designer, Product Designer, etc.  

## **Project Components**  

### **app.py**  

**Goal**: Main Flask application that handles web routes and file uploads  
**Algorithms/Techniques In Focus**: Flask web framework, file handling, template rendering  

**Description**:  
This file sets up the Flask web application, configures the upload folder, and defines routes for the home page and file upload processing. It securely handles file uploads, passes them to the model for analysis, and renders the appropriate templates.  

### **model.py**  

**Goal**: AI model integration and document processing  
**Algorithms/Techniques In Focus**: Zero-shot classification, text extraction, multi-format document processing  

**Description**:  
This file contains the core AI functionality, including the zero-shot classification model for analyzing resumes. It handles text extraction from various file formats (PDF, DOCX, TXT), including OCR for scanned PDFs, and classifies the resume content against job categories.  

### **index.html**  

**Goal**: Provide the upload interface for users  
**Algorithms/Techniques In Focus**: Responsive design, drag-and-drop file upload, visual feedback  

**Description**:  
This template creates a modern, responsive interface for users to upload their resumes. It includes animations and visual feedback to enhance the user experience.  

### **results.html**  

**Goal**: Display analysis results to users  
**Algorithms/Techniques In Focus**: Data visualization, responsive design, dynamic content rendering  

**Description**:  
This template presents the analysis results in a visually appealing format, showing the top matching role and a breakdown of all matches. It includes gauges and progress bars to visualize match percentages.  

## **Installation**  

```bash
# Clone the repository
git clone https://github.com/chigoziennani/chi-resume-scanner.git
cd chi-resume-scanner

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

```
The application will be available at http://127.0.0.1:5000/.

## **Requirements**
- Python 3.8+
- flask
- torch
- transformers
- werkzeug
- pdfplumber
- pdf2image
- pytesseract
- pillow
- python-docx

## **Future Enhancements**
- Expanded job role categories
- Detailed skill gap analysis
- Personalized resume improvement suggestions
- Resume comparison against job descriptions
- Fine-tuned models for specific industries
