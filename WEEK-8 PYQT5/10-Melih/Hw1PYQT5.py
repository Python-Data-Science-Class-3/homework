""" 

Developer : Melih Orhan Yilmaz
Date      : 26.01.2023

Application : PYQT5

Explanation : 
    • Create a push button to open pop up for getting time and set its geometry 
    • Create label to show time and complete status
    • Set label geometry, font size and align its text to center
    • Create four push button for starting the timer, pausing the timer , for resetting the timer and for exiting the timer.
    • Add icon to each button 
    • Create two actions in the menu bar for About the program and Exit the program. 

    • Add action to each button
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys

class MainScreen(QMainWindow):

    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("Dersler\Week_8\\3.timer\\timer.ui", self)
        self.count = 0
        self.start = False
        self.Buttons()

    def Buttons(self):
        self.setTimerButton.clicked.connect(self.get_seconds)
        self.startButton.clicked.connect(self.start_button) 
        self.stopButton.clicked.connect(self.stop_button) 
        self.resetButton.clicked.connect(self.reset_button) 


        self.actionAbout.triggered.connect(self.about_action)
        #self.actionExit.triggered.connect(self.exit_action)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def get_seconds(self):
        self.start = False

        text, okPressed = QInputDialog.getInt(self, "Dersler\Week_8\\3.timer\seconds.ui","Second:", 0, 0, 20, 1)
        if okPressed:
            self.labelTimer.setText(str(text))

    def start_button(self):
        self.start = True
 
        if self.count == 0:
            self.start = False
 
    def stop_button(self):
        self.start = False
 
    def reset_button(self):
        self.start = False
        self.count = 0
        self.labelTimer.setText("//TIMER//")
    
    def showTime(self):
 
        if self.start:
            self.count -= 1

            if self.count == 0:
                self.start = False
                self.labelTimer.setText("Completed !!!! ")
 
        if self.start:
            text = str(self.count / 10) + " s"
            self.labelTimer.setText(text)

    def about_action(self):
        QMessageBox.about(self.parent(), "About","This program has been created by Melih Orhan Yilmaz at 26.01.2023")
 
    #def exit_action(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainScreen()
    widget = QStackedWidget()
    
    widget.addWidget(window)
    widget.setFixedHeight(400)
    widget.setFixedWidth(400)
    widget.show()
    
    try:
        sys.exit(app.exec_())

    except:
        print("Exiting")

    



    
"""
    def go_to_screen2(self):
        screen2 = SecondScreen()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def go_to_screen3(self):
         screen3 = ThirdScreen()
         widget.addWidget(screen3)
         widget.setCurrentIndex(widget.currentIndex()+1)"""

"""class SecondScreen(QMainWindow):

    def __init__(self):
        super(SecondScreen, self).__init__()
        loadUi("Dersler\Week_8\\3.timer\seconds.ui", self)
        self.seconds = self.secondsBox.text()
        self.okButton.clicked.connect(self.go_to_mainscreen)
        self.cancelButton.clicked.connect(self.go_to_mainscreen)

    def go_to_mainscreen(self):
        screen1 = MainScreen()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()-1)
        #MainScreen.labelTimer.setText(self.seconds)
        #self.labelTimer.show(self.go_to_mainscreen)"""

"""class ThirdScreen(QWidget):

    def __init__(self):
        super(ThirdScreen, self).__init__()
        loadUi("Dersler\Week_8\\3.timer\\about.ui", self)"""
