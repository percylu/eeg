# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mianwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.eegWaveLineChart = QChartView(self.centralwidget)
        self.eegWaveLineChart.setMinimumSize(QtCore.QSize(800, 600))
        self.eegWaveLineChart.setObjectName("eegWaveLineChart")
        self.verticalLayout.addWidget(self.eegWaveLineChart)
        self.inputTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.verticalLayout.addWidget(self.inputTextEdit)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout.addWidget(self.startBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "开始"))
from PyQt5.QtChart import QChartView
