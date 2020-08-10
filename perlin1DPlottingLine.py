import sys
import math
import noise
from PyQt5 import QtCore, QtGui, QtWidgets

class PN1D(QtWidgets.QWidget):
    def __init__(self):
        super(PN1D, self).__init__()

        self.pal = QtGui.QPalette()
        self.pal.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(self.pal)

        self.pen = QtGui.QPen()
        self.pen.setColor(QtCore.Qt.white)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.frames)
        self.timer.start(1)
        self.frame = 0

    def frames(self):
        self.frame += 0.05
        self.update()


    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.setPen(self.pen)
        p.drawText(10, 20, str('{:.2f}'.format(self.frame)))

        p.save()
        p.translate(0, 50)
        for i in range(self.width()):
            p.drawPoint(i, math.sin((self.frame)+i/50)*50)
        p.restore()

        p.save()
        p.translate(0, 250)
        for i in range (self.width()):
            p.drawPoint(i, noise.pnoise1(self.frame+i/50)*100)
        p.restore()

        p.save()
        p.translate(0, 400)
        for i in range(self.width()):
            s = math.sin((self.frame)+i/50)*40
            n = noise.pnoise1(self.frame+i/50)*10
            p.drawPoint(i, n+s)
        p.restore()

        p.save()
        p.translate(self.width()/2, self.height()/2)
        p.drawEllipse(noise.pnoise1(self.frame+i/100)*self.width()/2, noise.pnoise1(self.frame+i/100, base=100)*self.height()/2, 20, 20)
        p.restore()










app = QtWidgets.QApplication(sys.argv)
PN1D = PN1D()
PN1D.show()
app.exec_()