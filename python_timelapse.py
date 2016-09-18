import os
import re
import time
import python_camera_client

OUTPUT_DIR = "/home/pi/camera_scripts/timelapse"

def get_file_num(file):
    num_str = re.match(r'image(\d+).jpg', file).group(1)
    return int(num_str)

def do_timelapse():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    existing_files = os.listdir(OUTPUT_DIR)
    numbers = [get_file_num(x) for x in existing_files]
    start_number = max(numbers) + 1

    image_data = python_camera_client.capture_image()
    with open(OUTPUT_DIR + "/image{}.jpg".format(start_number), "wb") as f:
        f.write(image_data)
        

if __name__=="__main__":
    do_timelapse()


