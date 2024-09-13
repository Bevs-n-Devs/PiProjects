import cv2
import numpy as np
import sys
import threading
import time
from imutils.video.pivideostream import PiVideoStream
from datetime import datetime
#import tflite_support
#from tflite_support.task import core
#from tflite_support.task import processor
#from tflite_support.task import vision

class CamFeed:
    """
    Provides the PiCam feed to the frontend
    """
    def __init__(self):
        print("Initializing PiCam Feed...", file=sys.stdout)
        self.vs = PiVideoStream().start()
        self.flip = False
        self.file_type = ".jpg"
        self.photo_string = "stream_photo"
        time.sleep(0.2)
        #self.frame = cv2.flip(self.frame,flipCode=-1)

        #self.detector = vision.ObjectDetector.create_from_file('lite-model_efficientdet_lite0_detection_default_1.tflite')

        #threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.vs.stop()

    def get_frame(self):
        self.frame = self.vs.read()
        ret, jpeg = cv2.imencode(self.file_type, self.frame)
        self.previous_frame = jpeg
        return jpeg.tobytes()

    def update(self):
        while True:
            self.get_frame()
