import sys

import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtCore import QThread, pyqtSignal


from View.ui import Ui_MainWindow

from Renderer.canvas import CanvasRenderer


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        # ==========================================
        # 主畫面創建
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Sin, Cos 波動畫顯示")

        self.config = {}
        self.updateConfig()

        self.canvasRenderer = None
        self.add_Canvas_To_Widget(parent=self.plot_widget, layoutInt=111)
        # ==========================================
        # 事件連結 Action Connect Spot
        self.drawButton.clicked.connect(self.draw)

        # 每當資料有更動就進行一次重畫
        self.comboBox.currentTextChanged.connect(self.change_Draw_Figure_Type)
        
    def draw(self):
        self.canvasRenderer.reset()
        self.updateConfig()
        self.canvasRenderer.plot_AnimationData(self.config)
        

    def change_Draw_Figure_Type(self, Value):
        """繪圖種類更改 --> 更新繪圖種類"""
        print(Value, self.comboBox.currentIndex())
        self.canvasRenderer.changeDrawType(self.comboBox.currentIndex())
        self.draw()


    def updateConfig(self):
        self.config["f"] = float(self.f_input.text())
        self.config["a"] = float(self.a_input.text())
        self.config["theta"] = float(self.theta_input.text())
        self.config["delta"] = float(self.delta_input.text())
    
    
    def add_Canvas_To_Widget(self, parent=None, layoutInt=111):
        """乎腳此function建構Matplotlib Renderer並加入parent widget中"""
        if self.canvasRenderer is None:
            # Canvas Setting
            self.canvasRenderer = CanvasRenderer(layoutInt=layoutInt)
            parent.addWidget(self.canvasRenderer) # Add canvasRenderer to plot widgets(Can up to 3)

app = None
window = None

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())