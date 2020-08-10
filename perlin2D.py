import sys
import math
import noise
from PyQt5 import QtCore, QtGui, QtWidgets

class PN2D(QtWidgets.QWidget):
    def __init__(self):
        super(PN2D, self).__init__()

        self.setGeometry(2500, 200, 400, 400)

        self.pal = QtGui.QPalette()
        self.pal.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(self.pal)

        self.pen = QtGui.QPen()
        self.pen.setColor(QtCore.Qt.white)

        self.slider_off = QtWidgets.QSlider()
        self.slider_off.setMinimum(0)
        self.slider_off.setMaximum(2000)
        self.slider_off.valueChanged.connect(self.frames)
        self.slider_off.setGeometry(20, 20, 30, self.height()-40)

        self.slider_off.setParent(self)

    def frames(self):
        self.update()


    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.setPen(self.pen)
        p.drawText(10, 20, str('{:.2f}'.format(self.slider_off.value()/1000)))

        for x in range (self.width()):
            for y in range (self.height()):
                self.pen.setColor(QtGui.QColor(x/self.width()*255, y/self.height()*255, 0))
                p.setPen(self.pen)
                p.drawPoint(x, y)










app = QtWidgets.QApplication(sys.argv)
PN2D = PN2D()
PN2D.show()
app.exec_()