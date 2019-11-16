from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
from view.mianwindow import *
import sys
class DynamicEEG(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(DynamicEEG, self).__init__()
        self.setupUi(self)
        self.initEegWaveLineChart()
        self.eegPointBuffer=[]
        self.startBtn.clicked.connect(self.onShowPushButtonClick)
    def initEegWaveLineChart(self):
        self.axisY_EEG=QValueAxis()
        self.axisX_EEG=QValueAxis()
        self.eegSeries=QLineSeries()
        self.eegWaveLine =QChart()

        self.eegWaveLine.addSeries(self.eegSeries)
        self.axisY_EEG.setRange(-350,1200)
        self.axisX_EEG.setRange(0,600)
        self.axisX_EEG.setTickCount(30)
        self.axisY_EEG.setTickCount(10)

        #设置坐标轴的颜色，粗细和设置网格显示
        self.axisX_EEG.setGridLinePen(QPen(Qt.red,1,Qt.DashDotDotLine,Qt.SquareCap,Qt.RoundJoin))
        self.axisY_EEG.setGridLinePen(QPen(Qt.red,1,Qt.DashDotDotLine,Qt.SquareCap,Qt.RoundJoin))

        #坐标轴样式
        self.axisX_EEG.setLinePen(QPen(Qt.red, 1, Qt.DashDotDotLine, Qt.SquareCap, Qt.RoundJoin));
        self.axisY_EEG.setLinePen(QPen(Qt.red, 1, Qt.DashDotDotLine, Qt.SquareCap, Qt.RoundJoin));


        #显示线框
        self.axisY_EEG.setGridLineVisible(True)
        self.axisX_EEG.setGridLineVisible(True)

        #不显示label具体数值
        self.axisX_EEG.setLabelsVisible(False)
        self.axisY_EEG.setLabelsVisible(False)

        #把坐标轴添加到chart
        self.eegWaveLine.addAxis(self.axisX_EEG,Qt.AlignBottom)
        self.eegWaveLine.addAxis(self.axisY_EEG,Qt.AlignLeft)

        #把曲线关联到坐标轴
        self.eegSeries.attachAxis(self.axisX_EEG)
        self.eegSeries.attachAxis(self.axisY_EEG)
        self.eegSeries.setColor(QColor(Qt.black))

        self.eegWaveLine.legend().hide()
        self.eegWaveLineChart.setChart(self.eegWaveLine)

    def onShowPushButtonClick(self):
        self.originList=[]
        self.originListIndex=0
        self.origin=self.inputTextEdit.toPlainText()
        if self.origin == "":
            return
        self.originList=self.origin.split(",")
        self.originListSize=len(self.originList)
        self.eegWaveDrawTimer=QTimer(self)
        self.eegWaveDrawTimer.start(8)
        self.eegWaveDrawTimer.timeout.connect(self.oneTimeOutAction)

    def oneTimeOutAction(self):
        if self.originListIndex>=self.originListSize:
            self.eegWaveDrawTimer.stop()
        else:
            tempInt16=int(self.originList[self.originListIndex])
            self.drawEegWave(self.originListIndex,tempInt16)
            self.originListIndex+=1
    def drawEegWave(self,axis_x,data):
        timeCounts=int(axis_x/600)
        if timeCounts > 0:
            axis_x=axis_x-timeCounts*600
            self.eegPointBuffer[axis_x].setY(data)
        else:
            self.eegPointBuffer.append(QPointF(axis_x,data))
        self.eegSeries.replace(self.eegPointBuffer)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    ui=DynamicEEG()
    ui.resize(800,600)
    ui.show()
    sys.exit(app.exec_())