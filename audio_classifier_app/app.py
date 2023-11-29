import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
#from audio_classifier import AudioClassifier  
# # Assuming you have the AudioClassifier module in a separate file

app = Flask(__name__)

# Set the path where uploaded audio files will be stored
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

#UPLOAD_FOLDER = 'uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'wav'}

#def classify_genre(self,audio_file_path):
        # Replace this with your actual model loading and classification logic
        # This is a placeholder implementation
        #return "jazz", 0.85

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling file upload and classification
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + '/' + filename
        file.save(file_path)

        # Make predictions using the AudioClassifier
        #predicted_genre, confidence_score = audio_classifier.classify_genre(file_path)
        predicted_genre, confidence_score = "jazz", 0.85

        # Render the results
        return render_template('result.html', filename=filename, predicted_genre=predicted_genre, confidence_score=confidence_score)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
