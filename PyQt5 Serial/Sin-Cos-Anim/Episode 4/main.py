import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.connectSlot()
        
        
    def connectSlot(self):
        self.button.clicked.connect(self.btnOnClicked)
        
        
    def btnOnClicked(self):
        print("Button 被按下了!")
        
app = None
window = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())