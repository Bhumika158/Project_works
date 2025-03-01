import torch
import cv2
import os

# Load YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s", source="local", pretrained=True)

input_folder = "output_frames/"
output_folder = "runs/detect/"
os.makedirs(output_folder, exist_ok=True)

for img_file in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img_file)
    
    # Perform inference using YOLO
    results = model(img_path)
    results.save(save_dir=output_folder)

print("✅ Car detection completed!")
