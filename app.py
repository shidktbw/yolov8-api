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
    model_file = request.files['model']
    image_file = request.files['file']
    
    model_filename = "models/" + str(random.randint(1, 1000000)) + ".pt"
    model_file.save(model_filename)

    model = YOLO(model_filename)
    
    image_filename = str(random.randint(1, 1000000)) + ".jpg"
    image_file.save(os.path.join('temp', image_filename))
    
    results = model.predict(source=os.path.join('temp', image_filename),save=True)
    
    latest_dir = max(glob.glob('runs/detect/predict*'), key=os.path.getctime)
    time.sleep(5)
    return render_template('index.html', filename=image_filename, latest_dir=latest_dir)




@app.route('/image/<path:path>')
def serve_image(path):
    path = path.replace('\\', '/')  
    return send_from_directory('', path)



if __name__ == '__main__':
    app.run(debug=True)
