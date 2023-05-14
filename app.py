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
    # Получить загруженный файл из запроса
    file = request.files['file']
    # Создать случайное имя файла изображения
    filename = str(random.randint(1, 1000000)) + ".jpg"
    # Сохранить файл во временной директории с новым именем
    file.save(os.path.join('temp', filename))
    # Вызвать вашу нейросеть для обработки изображения
    results = model.predict(source=os.path.join('temp', filename),save=True)
    # Получить последнюю созданную папку
    latest_dir = max(glob.glob('runs/detect/predict*'), key=os.path.getctime)
    # Добавить задержку в 5 секунд
    time.sleep(5)
    # Вернуть результаты в HTML-страницу
    return render_template('index.html', filename=filename, latest_dir=latest_dir)



@app.route('/image/<path:path>')
def serve_image(path):
    path = path.replace('\\', '/')  
    return send_from_directory('', path)



if __name__ == '__main__':
    app.run(debug=True)
