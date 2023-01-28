from PyQt5.QtWidgets import *
import sys
from ui_timer import *

class Pencere(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(Pencere,self).__init__()
        self.setupUi(self)
        
        self.ButtonStart.clicked.connect(self.baslat)
    def baslat(self):
        
        self.actionExit.clicked.connect(self.kapat)
        self.ButtonStart_2.clicked.connect(self.kapat)
    def kapat(self):
        
        self.ButtonPaus.clicked.connect(self.durdur)
    def durdur(self):
        
        self.ButtonReset.clicked.connect(self.resetle)
    def resetle(self):
        
        self.actionAbout.clicked.connect(self.bilgi)
    def bilgi(self):
        
        
        
        
        
        
            
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    pencere=Pencere()
    pencere.show()
    sys.exit(app.exec_())
    
            