# Mounting Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

#  installing Yolov8 and its Dependencies
%pip install ultralytics
import ultralytics
ultralytics.checks() # To check Yolo Version

# Install Roboflow for Dataset API integration  
!pip install roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="DQ084MQZOJFQ6IQMiCpH")
project = rf.workspace("object-detection-cfmul").project("waste-detection-0momv")
version = project.version(5)
dataset = version.download("yolov8")

from ultralytics import YOLO    # Importing Yolov8 from ultralytics
model=YOLO('yolov8n-seg.pt')    # selecting model as Yolo Nano Segmentation model

model.train(data = '/content/data.yaml',epochs=20)   # Training model with custom dataset

custom=YOLO('/content/runs/detect/train/weights/best.pt')   # Assign the trained weight to custom 

custom.predict('/content/add_data/test/images',save=True)   # Checking custom weight to check the model in image

!yolo detect predict model= '/content/runs/detect/train/weights/best.pt' source='/content/testing_video.mp4'  # Checking custom weights to check the model in Video
