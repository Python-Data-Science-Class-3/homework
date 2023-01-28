from PyQt5 import QtWidgets, QtCore, uic

class Timesettings(QtWidgets.QMainWindow):
    signal = QtCore.pyqtSignal(int)

    def __init__(self,limit):
        super(Timesettings,self).__init__()
        uic.loadUi("second.ui",self)
        self.limit.setValue(limit)

        self.setWindowTitle("Seconds  ???")
        self.okButton.clicked.connect(self.change)
        #self.limit.setMinimum(0)
        #self.limit.setMaximum(30)
        self.limit.valueChanged.connect(self.limit_stat)
    
    def limit_stat(self,val):
        self.stat.setText(str(round(float(val),1)))

    def change(self):
        time_in_secs = float(self.limit.value())
        self.signal.emit(int(time_in_secs))


