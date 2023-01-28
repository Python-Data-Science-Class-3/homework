from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUi

class Pencere(QMainWindow):
    

    
    def __init__(self):
        super(Pencere,self).__init__()
        loadUi("timer.ui",self)
         
        self.ButtonStart.clicked.connect(self.baslat)
        self.actionExit.clicked.connect(self.kapat)
        self.ButtonStart_2.clicked.connect(self.kapat)    
        self.ButtonPaus.clicked.connect(self.durdur)
        self.ButtonReset.clicked.connect(self.resetle)
        self.actionAbout.clicked.connect(self.bilgi)
        
    def baslat(self):
        self.ButtonStart.clicked.connect(pencere.startTimer)
        
        
        
    def kapat(self):
        self.ButtonStart_2.clicked.connect(pencere.close())
        
    def durdur(self):
        
        
    def resetle(self):
        self.ButtonReset.clicket.connect(pencere.startTimer)
        
        
    def bilgi(self):
        QMessageBox.about(self.parent(),"About","Bu bir geri sayim programidir.Qt designer ile tasarlanmis ve python dilinde programlanmistir")
        
        
        
        
        
        
        
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    pencere=Pencere()
    pencere.show()
    sys.exit(app.exec_())
    
            