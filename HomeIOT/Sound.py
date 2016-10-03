import pyaudio
import wave
import threading
import time
import requests
class Sound(threading.Thread):
    def __init__(self,lenght,upload,host):
        threading.Thread.__init__(self)
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.LENGTH = lenght
        self.Audio = pyaudio.PyAudio()
        self.Frames = []
        self.FileName = str(time.time())+".wav"
        self.Upload = int(upload)
        self.Host = host
    def run(self):
        self.Stream = self.Audio.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        for i in range(0,int(self.RATE/self.CHUNK*self.LENGTH)):
            data = self.Stream.read(self.CHUNK)
            self.Frames.append(data)
        self.Stream.stop_stream()
        self.Stream.close()
        self.Audio.terminate()
        waveFile = wave.open(self.FileName,'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.Audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(self.Frames))
        waveFile.close()
        if(self.Upload > 0):
            files = {'File': open(self.FileName, 'rb')}
            state = requests.post(self.Host, files=files,data={'Type':'Sound'})
            print "Upload Sound state: ",state
# ben = Sound(5,1,"http://localhost/HomeIOT/IOTAPI.php")
# ben.start()
