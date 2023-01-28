from PyQt5 import QtWidgets, QtCore, uic,QtGui
import sys
from timerwindow import Timesettings
from getstime import Timerthread

class Mainwindow(QtWidgets.QMainWindow):
    signal_to_sett = QtCore.pyqtSignal()

    def __init__(self,*args, **kwargs):
        super(Mainwindow,self).__init__()
        uic.loadUi("main.ui",self)
        self.setWindowTitle("Time Counter")
        self.time_in_secs = 1800
        self.pause.hide()
        self.thread = Timerthread(self.time_in_secs)
        
        self.timeset.clicked.connect(self.to_settings)
        self.start.clicked.connect(self.start_timer)
        self.pause.clicked.connect(self.pause_timer)
        self.reset.clicked.connect(self.reset_timer)
        self.actionAbout.triggered.connect(self.about_action)

    
    def to_settings(self):
        self.signal_to_sett.emit()

    def start_timer(self):
        self.start.hide()
        self.pause.show()
        self.thread.signal.connect(self.change_timer)
        self.thread.start()
               
        

    def change_timer(self,val):
        if val == -1:
            self.start.show()
            self.count.setText("Timer")
        
        

    def pause_timer(self):
        self.thread.flag = False
        self.pause.hide()
        self.start.show()

    def reset_timer(self):
        self.thread.flag = False
        self.count.setText("Timer")
        self.pause.hide()
        self.start.show()
    
    def about_action(self):
        self.activateWindow("about.ui")
   

class Controller:
    def show_main(self):
        self.main = Mainwindow()
        self.main.show()
        self.main.signal_to_sett.connect(self.show_settings)
    
    def show_settings(self):
        print("i am going to settings")
        self.settings = Timesettings(self.main.thread.limit_seconds)
        self.settings.signal.connect(self.change_limit)
        self.settings.show()

    def change_limit(self,val):
        self.main.thread.limit_seconds = val
        print (self.main.thread.limit_seconds)

class Aboutwindow:
    def __init__ (self):
        super(Aboutwindow,self).__init__()
        uic.loadUi("about.ui",self)
        self.actionabout.clicked.connect(self.go_to_about)

    def go_to_about(self):
        about = Aboutwindow()
        pass





app = QtWidgets.QApplication(sys.argv)
ctr = Controller()
ctr.show_main()
sys.exit(app.exec_())
