import os
import shutil
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from model import analyze_resume  # AI logic

app = Flask(__name__)

# Configure temporary upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# File extension check
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "resume" not in request.files:
            return redirect(request.url)

        file = request.files["resume"]
        if file.filename == "" or not allowed_file(file.filename):
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Process resume with AI model
        analysis = analyze_resume(filepath)

        # Cleanup the uploaded file after processing
        os.remove(filepath)

        return render_template("results.html", analysis=analysis)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)