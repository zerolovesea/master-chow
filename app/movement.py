import cv2
import time

class MovementDetect:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.width  = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.size = self.width, self.height
        self.fps = 2
        self.pre_frame = None
        self.script = []
    
    def detect(self):
        while (1):
            start = time.time()

            ret, frame = self.camera.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if not ret:
                print("Failed to open camera")
                break

            end = time.time()
            seconds = end - start

            if seconds < 1.0 / self.fps:
                time.sleep(1.0 / self.fps - seconds)

            gray_frame = cv2.resize(gray_frame, (480, 480))
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if self.pre_frame is None:
                self.pre_frame = gray_frame
            else:
                img_delta = cv2.absdiff(self.pre_frame, gray_frame)
                thresh = cv2.threshold(img_delta, 30, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=2)
                contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in contours:
                    if cv2.contourArea(c) < 1000:
                        return False
                    else:
                        return True