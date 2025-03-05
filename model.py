import os
import pdfplumber
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
from transformers import pipeline

# Load AI Model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define job categories
job_categories = [
    # Software & Development
    "Software Engineer", "Frontend Developer", "Backend Developer", "Full Stack Developer",
    "Mobile App Developer", "Game Developer", "Cloud Engineer", "DevOps Engineer",
    "Embedded Systems Engineer", "Security Engineer",

    # Data & AI/ML
    "Data Scientist", "Data Engineer", "Machine Learning Engineer", "AI Research Scientist",
    "Data Analyst", "Big Data Engineer", "Business Intelligence Analyst",

    # Cloud & Infrastructure
    "Cloud Architect", "Site Reliability Engineer",

    # Hardware & Embedded
    "Hardware Engineer", "Electrical Engineer", "Computer Engineer", "Robotics Engineer",
    "FPGA Engineer", "Power Electronics Engineer", "Battery Systems Engineer", "IoT Engineer",
    "Circuit Design Engineer",

    # General Engineering
    "Mechanical Engineer", "Civil Engineer", "Aerospace Engineer", "Automotive Engineer",
    "Biomedical Engineer", "Chemical Engineer", "Industrial Engineer", "Manufacturing Engineer",
    "Petroleum Engineer", "Structural Engineer", "Power Systems Engineer",

    # Project & Program Management
    "Product Manager", "Project Manager",

    # IT & Business Analysis
    "IT Analyst", "Business Analyst", "Technical Analyst", "Solutions Architect",
    "Technical Writer", "Business Systems Analyst", "Technology Consultant",
    "IT Project Manager", "Systems Administrator", "IT Support Specialist",
    "Network Administrator", "Helpdesk Technician",

    # UX/UI & Design
    "UI/UX Developer", "Visual Designer", "Product Designer", "Motion Graphics Designer",

    # Other Tech Roles
    "Game Designer", "Game Programmer", "Augmented Reality Developer", "Virtual Reality Developer",
    "API Developer", "DevSecOps Engineer",
    "Digital Forensics Expert", "Computer Graphics Engineer", "Game Engine Developer"
]

def extract_text_from_pdf(filepath):
    text = ""
    try:
        # First attempt text extraction with pdfplumber
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join(
                page.extract_text() for page in pdf.pages if page.extract_text()
            )

        if text.strip():
            return text  # Successfully extracted text-based content

        # If no text was extracted, use OCR for scanned/image-based PDFs
        images = convert_from_path(filepath)
        text = "\n".join(
            pytesseract.image_to_string(img) for img in images
        )

    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

    return text if text.strip() else "No readable text found in PDF"

def analyze_resume(filepath, engineer_threshold=0.50):
    text = ""
    file_ext = os.path.splitext(filepath)[1].lower()

    if file_ext == ".txt":
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            return {"error": f"Error reading text file: {str(e)}"}

    elif file_ext == ".docx":
        try:
            doc = Document(filepath)
            text = "\n".join([p.text for p in doc.paragraphs])
        except Exception as e:
            return {"error": f"Error extracting text from DOCX: {str(e)}"}

    elif file_ext == ".pdf":
        text = extract_text_from_pdf(filepath)
        if text.startswith("Error"):
            return {"error": text}

    else:
        return {"error": f"Unsupported file extension: {file_ext}"}

    if not text.strip():
        return {"error": "No text found in resume"}

    # Separate engineer roles from the rest
    engineer_roles = [r for r in job_categories if "engineer" in r.lower()]
    other_roles = [r for r in job_categories if r not in engineer_roles]

    # Phase 1: classify only among engineer roles
    engineer_result = classifier(
        text, engineer_roles, multi_label=True
    )
    top_engineer_score = engineer_result["scores"][0]
    top_engineer_label = engineer_result["labels"][0]

    # If top engineer score is high enough, skip other roles
    if top_engineer_score >= engineer_threshold:
        return {
            "categories": dict(zip(engineer_result["labels"], engineer_result["scores"])),
            "top_category": top_engineer_label
        }
    else:
        # Otherwise, classify on all roles
        full_result = classifier(
            text, job_categories, multi_label=True
        )
        return {
            "categories": dict(zip(full_result["labels"], full_result["scores"])),
            "top_category": full_result["labels"][0]
        }