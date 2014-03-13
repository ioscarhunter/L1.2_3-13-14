from PySide.QtCore import *
from PySide.QtGui import *
class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,255,0))
        p.drawPolygon([
           
            QPoint(130,100),QPoint(100,150),
            QPoint(70,100),QPoint(100,110),
             QPoint(150,60),QPoint(400,50),
            ])
      
        p.drawImage(QRect(200,100,320,320),self.rabbit)
        p.end()
def main():
    app  = QApplication([])
    draw = Simple_drawing_window2()
    draw.show()
    app.exec_()
if __name__ =="main":
    main()

