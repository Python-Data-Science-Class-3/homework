from PyQt5.QtCore import *
import time, sys

class Timerthread(QThread):
    signal = pyqtSignal(int)

    def __init__(self,limit):
        super(Timerthread,self).__init__()
        self.limit_seconds = limit
    
    def run(self):
        i = self.limit_seconds
        self.flag = False
        while i > 0 : 
            if self.flag :
                break
            self.signal.emit(i)
            time.sleep(1)

            i -= 1
        self.signal.emit(-1)
