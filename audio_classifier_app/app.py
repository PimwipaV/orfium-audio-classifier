import os
from flask import Flask, render_template, request, redirect, url_for

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            raise ValueError("No file part in the request.")

        file = request.files['file']

        if file.filename == '':
            raise ValueError("No selected file.")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Place your actual model loading and classification logic here
            # For now, using placeholder values
            predicted_genre, confidence_score = "jazz", 0.85

            return render_template('result.html', filename=filename, predicted_genre=predicted_genre, confidence_score=confidence_score)

        else:
            raise ValueError("Invalid file extension. Allowed extensions are: {}".format(ALLOWED_EXTENSIONS))

    except Exception as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
