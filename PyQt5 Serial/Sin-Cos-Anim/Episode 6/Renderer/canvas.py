import matplotlib
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import QtWidgets, QtCore, QtGui

import numpy as np

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# matplotlib.rcParams["font.family"] = ["SimHei"] # 正常顯示中文用
matplotlib.rcParams["axes.unicode_minus"] = False # 正常顯示負號用


# Matplotlib canvas class to create figure
class CanvasRenderer(FigureCanvas):

    FRAME_PER_SECOND = 20
    updateTime = 0

    zhfont1 = matplotlib.font_manager.FontProperties(fname="resource/font/msjh.ttc")


    def __init__(self, width=5, height=4, dpi=100, layoutInt=111):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.suptitle("Sin 正弦波", fontproperties=self.zhfont1)

        self.axes = self.fig.add_subplot(layoutInt)
        self.axes.clear()
        self.axes.grid(True)

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        # 也可以這樣寫
        # super().__init__(self.fig)
        # super().setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # super().updateGeometry()
        
        self.timer = None
        self.plot_AnimationData()
        
    def plot_AnimationData(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_AnimationData)
        self.timer.start(1000/self.FRAME_PER_SECOND)
        
    def update_AnimationData(self):
    
        # 次數增加
        self.updateTime = self.updateTime + 1

        # 插入資料
        self.X = np.linspace(self.updateTime, self.updateTime + 20, 100)
        self.Y = np.sin(self.X)
        
        # 繪圖
        self.axes.set_xlim(self.updateTime, self.updateTime + 20)
        self.axes.plot(self.X, self.Y, "c")

        self.axes.set_xlabel("時間", fontproperties=self.zhfont1)
        self.axes.set_ylabel("震幅", fontproperties=self.zhfont1)
        self.axes.grid(True)
        self.draw()