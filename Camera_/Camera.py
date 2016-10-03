import cv2 as cv
import threading
import time
class Camera(threading.Thread):
    def __init__(self,host,type):
        threading.Thread.__init__(self)
        self.Host = host
        self.Cam = cv.VideoCapture(self.Host)
        self.Image = None
        self.isRunning = True
        self.Type = type
        self.Started = int(time.time())
        self.FileName = ""
    def run(self):
        if(self.Type == 0):
            x = 2
            while(x>0):
                state,image = self.Cam.read()
                self.Image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
                x -=1
            self.FileName = "Image"+str(int(time.time()))+".png"
            cv.imwrite(self.FileName,self.Image)

        if(self.Type > 0):
            x = 100
            while(x>0):
                state,image = self.Cam.read()
                self.Image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
                x -=1
            self.FileName = "Image"+str(int(time.time()))+".png"
            cv.imwrite(self.FileName,self.Image)

Cam = Camera(0,0)
Cam.start()
Cam.join()
print Cam.FileName
# cam = cv.VideoCapture(0)
# x = 1
# while(x>0):
#     st,img = cam.read()
#     img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     cv.imshow("Camera_ ",img)
#     cv.waitKey(10)
#     x = x - 1

