import threading
import urllib,urllib2,os
import time
import json
import serial
import Camera
import Sound
import requests



class HomeIOT(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.IOTHost = "http://localhost/HomeIOT/IOTAPI.php"
        self.Data = urllib.urlencode(dict(HomeIOT='Biniam'))
        self.Port = serial.Serial("/dev/cu.usbmodemFD121")
        self.Init_Sensors()
        self.Camera = Camera.Camera(0,0)
    def Init_Sensors(self):
        datagene = open("images/Image1475346306.png","rb")
        length = os.path.getsize("images/Image1475346306.png")
        request = urllib2.Request(self.IOTHost,datagene)
        request.add_header("Cache-Control","no-cache")
        request.add_header("Content-Length",'%d'%length)
        request.add_header("Content-Type",'image/png')
        res = urllib2.urlopen(request).read()
        self.Conn = urllib.urlopen(self.IOTHost,urllib.urlencode(dict(Type=open("images/Image1475346306.png","rb"),Port='13',State='0')))

    def run(self):
        while(True):
            self.Conn = urllib.urlopen(self.IOTHost,self.Data)
            res = self.Conn.read()
            print "Found\n",res
            SensorsConf = json.loads(res)['SensorConf']
            IOTTasks = json.loads(res)['IOTTask']
            self.UpdateSensorConf(SensorsConf)
            self.UpdateIOTask(IOTTasks)
            time.sleep(1)
    def SendSerial(self,command):
        pass
    def UpdateSensorConf(self,configurations):
        for conf in configurations:
            conf = json.loads(conf['sensorConf'])
            command = str(conf['Type'])+","+str(conf['Port'])+","+str(conf['State'])+","
            self.Port.write(command)
            print command
    def UpdateIOTask(self,iotTasks):
        for task in iotTasks:
            t1 = json.loads(task['task'])
            print t1
            type = t1['Type']
            if(type == 'Photo'):
                file_name = self.Camera.TakeCamera()
                files = {'File': open(file_name, 'rb')}
                state = requests.post(self.IOTHost, files=files,data={'Type':'Image'})
                print "Uploading:\n",state
            if(type == "Sound"):
                length = int(t1['Len'])
                sound = Sound.Sound(5,1,self.IOTHost).start()


IOT = HomeIOT()
IOT.start()


