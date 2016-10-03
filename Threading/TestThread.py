import threading
import time
class MyThread(threading.Thread):
    def __init__(self,sleep,name):
        threading.Thread.__init__(self)
        self.Sleep = sleep
        self.Name = name
        self.Count = 0
    def run(self):
        while(True):
            print self.Name+">> Time is: "+str(time.time())
            time.sleep(self.Sleep)
            self.Count += 1

th1 = MyThread(1,"One")
th2 = MyThread(2.3,"Two")
th1.start()
th2.start()
time.sleep(5)
th1.join()
print "One--> "+str(th1.Count)
print "Two--> "+str(th2.Count)





