
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

import numpy as np

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib Setting
# matplotlib.rcParams["font.family"] = ["SimHei"] # 正常顯示中文用
matplotlib.rcParams["axes.unicode_minus"] = False # 正常顯示負號用

import random



# Matplotlib canvas class to create figure
class CanvasRenderer(FigureCanvas):

    FRAME_PER_SECOND = 20

    updateTime = 0

    DrawType = 0

    zhfont1 = matplotlib.font_manager.FontProperties(fname="resource/font/msjh.ttc")
    ani = None

    def __init__(self, width=5, height=4, dpi=100, layoutInt=111):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.suptitle("Sin 正弦波", fontproperties=self.zhfont1)

        self.axes = self.fig.add_subplot(layoutInt)
        self.axes.clear()
        self.axes.grid(True)

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.timer = None

    def changeDrawType(self, drawType):
        self.reset()

        # self.fig.clf()

        if drawType == 0:
            self.DrawType = drawType
            self.fig.suptitle("Sin 正弦波", fontproperties=self.zhfont1)

        elif drawType == 1:
            self.DrawType = drawType
            self.fig.suptitle("Cos 餘弦波", fontproperties=self.zhfont1)

        # self.axes.clear()
        # self.axes.grid(True)


    def plot_AnimationData(self, config):

        self.X = None
        self.Y = None
        self.config = config

        # ========================================================================================
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_AnimationData)
        self.timer.start(1000/self.FRAME_PER_SECOND)




    def update_AnimationData(self):

        # 怕跑太多迴圈，所以 利用 @Params updateTime 確認跑的次數
        # 超過最大值 20 就
        # 1. 停止 timer
        # 2. timer 回歸 None
        # 3. updateTime 歸零
        if self.updateTime >= 100000 and self.timer is not None:
            self.timer.stop()
            self.timer = None
            self.updateTime = 0
            self.X = None
            self.Y = None


        # 次數增加
        self.updateTime = self.updateTime + 1


        # 插入資料
        self.X = np.linspace(self.updateTime, self.updateTime + 20, 100)
        if self.DrawType == 0:
            self.Y = self.config["a"] * np.sin(self.config["f"] * self.X + self.config["theta"]) + self.config["delta"]
        elif self.DrawType == 1:
            self.Y = self.config["a"] * np.cos(self.config["f"] * self.X + self.config["theta"]) + self.config["delta"]


        # 繪圖
        self.axes.set_xlim(self.updateTime,self.updateTime + 20)

        self.axes.plot(self.X, self.Y, "c")

        self.axes.set_xlabel("時間", fontproperties=self.zhfont1)
        self.axes.set_ylabel("震幅", fontproperties=self.zhfont1)
        self.axes.grid(True)
        self.draw()

    def clearCanvas(self):
        # self.fig.clf()
        self.axes.clear()
        self.axes.grid(True)


    def reset(self):
        """讓 MainWindow 較好呼叫 回歸初始狀態"""
        if self.timer is not None:
            self.timer.stop()
            self.timer = None

        self.X = None
        self.Y = None
        self.updateTime = 0
        self.axes.clear()
        self.axes.grid(True)