import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_main import *
from Ui_about import *
from Ui_time_setter import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Main_Window(QMainWindow, Ui_main_window): 

    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Timer App")

        self.count = 0
        self.start = False
        
        self.mainwdw_action_about.triggered.connect(self.show_info)
        self.mainwdw_action_exit.triggered.connect(self.exit_app)
        self.mainwdw_action_main.triggered.connect(self.go_main)

        self.mainwdw_btn_settime.clicked.connect(self.open_setter)
        self.mainwdw_btn_play.clicked.connect(self.start_timer)
        self.mainwdw_btn_pause.clicked.connect(self.pause_timer)
        self.mainwdw_btn_reset.clicked.connect(self.reset_timer)
        self.mainwdw_btn_exit.clicked.connect(self.exit_app)
        
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

    def open_setter(self):
        self.setter = Setter_Window()
        self.main = Main_Window()
        widget.addWidget(self.setter)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_time(self):
        if self.start:
            self.count -= 1
            self.mainwdw_lbl_showtime.setText(str(self.count))
            if self.count == 0:
                self.start = False

    def start_timer(self):
        self.setter = Setter_Window()
        self.count = int(self.mainwdw_lbl_showtime.text())

        self.start = True
        if self.count == 0:
            self.start = False
    
    def pause_timer(self):
        self.start = False
    
    def reset_timer(self):
        self.start = False
        self.mainwdw_lbl_showtime.setText("0")

    def show_info(self):
        info = Info_Window()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # QMessageBox.about(self.parent(), "About","Melike Kaya\nBrussels")
    
    def go_main(self):
        main = Main_Window()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def exit_app(self):
        sys.exit(app.exec_())

class Setter_Window(QMainWindow, Ui_setter_window):
    def __init__(self):
        super(Setter_Window, self).__init__()
        self.setupUi(self)
        self.setterwdw_btn_set.clicked.connect(self.time_setter)
        self.seconds = self.setterwdw_spinbox_seconds.value()

    def time_setter(self):
        self.main = Main_Window()
        self.seconds = self.setterwdw_spinbox_seconds.value()
        widget.addWidget(self.main)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.main.mainwdw_lbl_showtime.setText(str(self.seconds))

class Info_Window(QMainWindow, Ui_info_window):
    def __init__(self):
        super(Info_Window, self).__init__()
        self.setupUi(self)
        self.infowdw_btn_return.clicked.connect(self.return_back)
        self.infowdw_btn_exit.clicked.connect(self.exit_app)
    
    def return_back(self):
        main = Main_Window()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def exit_app(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = Main_Window()    
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(app_window)
    widget.show()
    try:
        sys.exit(app.exec_())

    except:
        print("Exiting")
