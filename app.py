from flask import Flask, render_template, request, send_from_directory
from ultralytics import YOLO
import os
import time
import random
import glob


app = Flask(__name__)
model = YOLO("yolov8n.pt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the model file from the request
    model_file = request.files['model']
    # Get the uploaded file from the request
    image_file = request.files['file']
    
    # Create a unique file name for the model
    model_filename = "models/" + str(random.randint(1, 1000000)) + ".pt"
    # Save the model file
    model_file.save(model_filename)

    # Create an instance of the YOLO model with the loaded model
    model = YOLO(model_filename)
    
    # Create a random image file name
    image_filename = str(random.randint(1, 1000000)) + ".jpg"
    # Save the file to the temporary directory with the new name
    image_file.save(os.path.join('temp', image_filename))
    
    # Call neural network to process the image
    results = model.predict(source=os.path.join('temp', image_filename),save=True)
    
    # Get the latest created directory
    latest_dir = max(glob.glob('runs/detect/predict*'), key=os.path.getctime)
    # Add a 5-second delay
    time.sleep(5)
    # Return the results to the HTML page
    return render_template('index.html', filename=image_filename, latest_dir=latest_dir)




@app.route('/image/<path:path>')
def serve_image(path):
    path = path.replace('\\', '/')  
    return send_from_directory('', path)



if __name__ == '__main__':
    app.run(debug=True)
