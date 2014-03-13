from PySide.QtCore import *
from PySide.QtGui import *
class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(229,136,56))
        p.drawPolygon([
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100),QPoint(100,150),
            ])
        p.setPen(QColor(163,243,82))
        p.setBrush(QColor(95,155,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([
            QPoint(50,200),QPoint(150,200),QPoint(50,400),QPoint(150,400)])

        p.drawImage(QRect(200,100,320,277),self.rabbit)
        p.end()


app  = QApplication([])

draw = Simple_drawing_window1()
draw.show()

app.exec_()