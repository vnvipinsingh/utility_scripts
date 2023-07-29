import os
from moviepy.editor import VideoFileClip

def calculate_total_time(directory):
    total_duration = 0
    files = os.listdir(directory)
    for i, file in enumerate(files):
        file_abs_path = os.path.join(directory, file)
        if file.lower().endswith(('.mp4')):
            clip = VideoFileClip(file_abs_path)
            total_duration += clip.duration
    return total_duration

directory = os.getcwd()
total_duration = calculate_total_time(directory)
print(f"{total_duration} seconds")
print(f"{total_duration/(60)} minutes")
print(f"{total_duration/(60*60)} hour")
