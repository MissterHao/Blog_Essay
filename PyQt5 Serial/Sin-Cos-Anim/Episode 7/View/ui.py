# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 722)
        MainWindow.setStyleSheet("QPushButton, QComboBox{\n"
"/*qproperty-alignment: \"AlignVCenter | AlignHCenter\";*/\n"
"font: 63 12pt \"Adobe 繁黑體 Std B\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"qproperty-alignment: \"AlignVCenter | AlignHCenter\";\n"
"font: 63 12pt \"Adobe 繁黑體 Std B\";\n"
"}\n"
"\n"
"QLabel{\n"
"qproperty-alignment: \"AlignVCenter | AlignHCenter\";\n"
"font: 63 12pt \"Adobe 繁黑體 Std B\";\n"
"}\n"
"QPlainTextEdit {\n"
"    maximumBlockCount:1;\n"
"}\n"
"\n"
"QMainWindow{\n"
"/*background-color: red;*/\n"
"\n"
"}\n"
"\n"
"\n"
"#centralwidget {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(87, 255, 140, 255), stop:1 rgba(117, 210, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 140, 681, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.plot_widget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.plot_widget.setContentsMargins(0, 0, 0, 0)
        self.plot_widget.setObjectName("plot_widget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 140, 361, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(120, 50))
        self.label.setMaximumSize(QtCore.QSize(150, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.a_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.a_input.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.a_input.setFont(font)
        self.a_input.setAlignment(QtCore.Qt.AlignCenter)
        self.a_input.setObjectName("a_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.a_input)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 50))
        self.label_2.setMaximumSize(QtCore.QSize(150, 50))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 50))
        self.label_3.setMaximumSize(QtCore.QSize(150, 50))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(120, 50))
        self.label_4.setMaximumSize(QtCore.QSize(150, 50))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.delta_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.delta_input.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.delta_input.setFont(font)
        self.delta_input.setObjectName("delta_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.delta_input)
        self.theta_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.theta_input.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.theta_input.setFont(font)
        self.theta_input.setObjectName("theta_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.theta_input)
        self.f_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.f_input.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.f_input.setFont(font)
        self.f_input.setObjectName("f_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.f_input)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(232, 50))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 50))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(120, 50))
        self.label_5.setMaximumSize(QtCore.QSize(150, 50))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(360, 30, 541, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 75 26pt \"微軟正黑體\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.drawButton = QtWidgets.QPushButton(self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(50, 490, 361, 50))
        self.drawButton.setMinimumSize(QtCore.QSize(352, 50))
        self.drawButton.setObjectName("drawButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "震幅(A)"))
        self.a_input.setText(_translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "角頻率"))
        self.label_3.setText(_translate("MainWindow", "平移量"))
        self.label_4.setText(_translate("MainWindow", "初始角度"))
        self.delta_input.setText(_translate("MainWindow", "1"))
        self.theta_input.setText(_translate("MainWindow", "0"))
        self.f_input.setText(_translate("MainWindow", "2"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sin 正弦波"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cos 餘弦波"))
        self.label_5.setText(_translate("MainWindow", "波型"))
        self.title.setText(_translate("MainWindow", "Sin, Cos 波動畫顯示"))
        self.drawButton.setText(_translate("MainWindow", "畫圖"))

