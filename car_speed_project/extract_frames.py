import cv2
import os

video_path = "input_video/IMG_5678.mp4"  # Change this to your video file
output_frames_dir = "output_frames"
os.makedirs(output_frames_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))  # Get FPS
frame_interval = frame_rate // 2  # Extract every half-second

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frame_interval == 0:
        frame_filename = f"{output_frames_dir}/frame_{frame_count}.jpg"
        cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print("✅ Frames extracted successfully!")
