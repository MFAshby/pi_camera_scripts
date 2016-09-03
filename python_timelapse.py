import os
import time
import python_camera_client
import itertools

OUTPUT_DIR = "timelapse"
INTERVAL_SECONDS = 300


def start_timelapse():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for i in itertools.count(start=0, step=1):
        image_data = python_camera_client.capture_image()
        with open(OUTPUT_DIR + "/image{}.jpg".format(i), "wb") as f:
            f.write(image_data)
        time.sleep(INTERVAL_SECONDS)
        

if __name__=="__main__":
    start_timelapse()


