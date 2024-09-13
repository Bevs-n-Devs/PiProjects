import cv2
import numpy as np
import subprocess
import sys
import threading
import time


p = subprocess.run(["uname -m"],shell=True, capture_output=True) 
sysarch = p.stdout.decode('utf-8')
isPi4 = True
if (sysarch.find("arch32") > -1):
    isPi4 = False
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
        self.file_type = ".jpg"
        self.photo_string = "stream_photo"
        if not isPi4:
            self.vs = PiVideoStream().start()
            self.flip = False
            time.sleep(0.2)
        else:
            self.cap = cv2.VideoCapture(0)
            #self.frame = cv2.flip(self.frame,flipCode=-1)

        #self.detector = vision.ObjectDetector.create_from_file('lite-model_efficientdet_lite0_detection_default_1.tflite')

        #threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        if Pi4:
            self.cap.stop()
            return

        self.vs.stop()

    def get_frame(self):
        if not isPi4:
            ret, self.frame = self.vs.read()
            jpeg = cv2.imencode(self.file_type, self.frame)
            self.previous_frame = jpeg
            return jpeg.tobytes()
        
        ret, self.frame = self.cap.read()
        ret, jpeg = cv2.imencode(self.file_type, self.frame)
        self.previous_frame = jpeg.tobytes()

        return jpeg.tobytes()

    def update(self):
        while True:
            self.get_frame()
