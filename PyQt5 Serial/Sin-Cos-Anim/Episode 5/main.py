import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from View.ui import Ui_MainWindow

from Renderer.canvas import CanvasRenderer

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.addCanvasToWidget(self.plot_widget) # 擴充 UI

    def addCanvasToWidget(self, parent=None):
        self.canvasRenderer = CanvasRenderer()
        parent.addWidget(self.canvasRenderer)

        
app = None
window = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())