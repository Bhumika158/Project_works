import pandas as pd
import numpy as np

FPS = 60
pixel_to_meter_ratio = 0.0074  # Adjust this based on lane width in pixels

df = pd.read_csv("car_positions_tracked.csv", index_col=0)
car_speed_data = {}

for frame in range(len(df) - 1):
    for car_idx in range(len(df.iloc[frame])):
        if pd.notna(df.iloc[frame, car_idx]) and pd.notna(df.iloc[frame+1, car_idx]):
            car_id, x1, y1 = eval(df.iloc[frame, car_idx])
            _, x2, y2 = eval(df.iloc[frame+1, car_idx])
            pixel_distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            real_distance = pixel_distance * pixel_to_meter_ratio
            speed_mps = real_distance * FPS
            speed_kmph = speed_mps * 3.6
            car_speed_data.setdefault(car_id, []).append(speed_kmph)

print("🚗 Average Speeds (km/h):")
for car_id, speeds in car_speed_data.items():
    avg_speed = np.median(speeds)
    print(f"Car {car_id}: {avg_speed:.2f} km/h")
