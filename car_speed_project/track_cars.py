import os
import cv2
import numpy as np
import pandas as pd
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize DeepSORT Tracker
tracker = DeepSort(max_age=40, n_init=1, nms_max_overlap=1.0)

label_path = "runs/detect/"
frame_path = "output_frames/"
output_path = "annotated_frames/"
os.makedirs(output_path, exist_ok=True)

car_positions = {}

for frame_file in sorted(os.listdir(frame_path)):
    img_path = os.path.join(frame_path, frame_file)
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    detections = []

    # Read bounding boxes from YOLO
    with open(os.path.join(label_path, frame_file.replace(".jpg", ".txt")), "r") as f:
        for line in f.readlines():
            values = line.strip().split()
            cls, x_center, y_center, width, height = map(float, values)
            x1 = int((x_center - width / 2) * w)
            y1 = int((y_center - height / 2) * h)
            x2 = int((x_center + width / 2) * w)
            y2 = int((y_center + height / 2) * h)
            detections.append(([x1, y1, x2, y2], 1.0))  # Confidence = 1.0

    tracked_objects = tracker.update_tracks(detections, frame=img)

    for track in tracked_objects:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()  # Get bounding box
        x1, y1, x2, y2 = map(int, ltrb)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"Car {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        car_positions.setdefault(frame_file, []).append((track_id, (x1 + x2) // 2, (y1 + y2) // 2))

    cv2.imwrite(os.path.join(output_path, frame_file), img)

df = pd.DataFrame.from_dict(car_positions, orient='index')
df.to_csv("car_positions_tracked.csv")
print("✅ Car tracking completed!")
