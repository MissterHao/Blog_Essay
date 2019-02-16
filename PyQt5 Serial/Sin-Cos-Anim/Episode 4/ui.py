
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.resize(1200, 800)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("""#centralwidget {
            background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(87, 255, 140, 255), stop:1 rgba(117, 210, 255, 255));
            }"""
        )
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setText("Hello")
        self.button.setStyleSheet(
            """
                /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));*/
                background-color: white;
                border-radius: 15px;
                border-radius:
                    30px;
                border-style:
                    solid;
                border-width:
                    10px;
                border-color: green;
                font: 63 20pt "Adobe 繁黑體 Std B";
            """
        )
        
        MainWindow.setCentralWidget(self.centralwidget)
