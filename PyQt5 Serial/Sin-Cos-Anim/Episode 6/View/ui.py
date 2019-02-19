
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
        
        self.plot_widget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.plot_widget.setContentsMargins(100, 100, 100, 100)
        self.plot_widget.setObjectName("plot_widget")
        
        MainWindow.setCentralWidget(self.centralwidget)
