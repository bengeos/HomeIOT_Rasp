import cv2 as cv
import time
import urllib

class Camera():
    def __init__(self,host,type):
        self.SetUp(host,type)
        self.Cam = cv.VideoCapture(self.Host)
    def SetUp(self,host,type):
        self.Host = host
        self.Image = None
        self.isRunning = True
        self.Started = int(time.time())
        self.Length = int(type)
        self.FileName = ""
    def TakeCamera(self):
        if(self.Length == 0):
            x = 2
            while(x>0):
                state,image = self.Cam.read()
                self.Image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
                x -=1
            self.FileName = "images/Image"+str(int(time.time()))+".png"
            cv.imwrite(self.FileName,self.Image)

        if(self.Length > 0):
            self.Started = int(time.time())
            self.FileName = "images/Image"+str(int(time.time()))+".avi"
            fourcc = cv.cv.CV_FOURCC(*'XVID')
            self.VideoWritter = cv.VideoWriter(self.FileName,-1,20.0,(680,480))
            while(self.Started < self.Started + self.Length and self.Cam.isOpened()):
                state,image = self.Cam.read()
                image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
                self.VideoWritter.write(image)
                self.Started = int(time.time())
                print image
                cv.waitKey(10)
        return self.FileName
