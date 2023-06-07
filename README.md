# yolov8-api

![Снимок экрана 2023-06-07 173430](https://github.com/shidktbw/yolov8-api/assets/112849918/531851d2-1fd9-465c-9b17-77f8f0b52e53)



This is a Flask API implementation for YOLOv8, an object detection model. The API allows you to upload an image and perform object detection using the YOLOv8 model. The detected objects are then returned to the user along with the annotated image.

# Notes
The uploaded YOLOv8 model file will be temporarily saved in the models directory.
The uploaded image file will be temporarily saved in the temp directory.
The annotated image with the detected objects will be saved in a directory with a name starting with predict under the runs/detect directory.
There is a 5-second delay added after saving the annotated image to ensure it is available for display.
