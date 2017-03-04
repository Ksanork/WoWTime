import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel

from src.GUI.PrettyWidgets.PrettyWidget import PrettyWidget


# klasa przeciąża zdarzenia myszy

class DragDialog(QDialog, PrettyWidget):
    __posX = None
    __posY = None

    __icon = None

    DIALOG_MARGIN = 0

    def __init__(self, parent=None, img=None):
        super().__init__(parent)

        try:
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)

            self.__icon = QLabel()
            if img:
                self.__icon.setPixmap(QPixmap(img))
            layout.addWidget(self.__icon)
            self.setLayout(layout)

            self.setCursor(Qt.OpenHandCursor)
        except:
            print(sys.exc_info())

    def setPixmap(self, pixmap):
        self.__icon.setPixmap(pixmap)
        self.setFixedSize(pixmap.width() + self.DIALOG_MARGIN, pixmap.height() + self.DIALOG_MARGIN)

    def mousePressEvent(self, QMouseEvent):
        self.__posX = QMouseEvent.pos().x()
        self.__posY = QMouseEvent.pos().y()
        # self.__isPressed = True
        self.setCursor(Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, QMouseEvent):
        # self.__isPressed = None
        self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, QMouseEvent):
        # self.__showStatusTimer.stop()
        # self.hideStatusDialog()

        self.setGeometry(self.mapToGlobal(QMouseEvent.pos()).x() - self.__posX,
                         self.mapToGlobal(QMouseEvent.pos()).y() - self.__posY,
                         self.width(), self.height())
