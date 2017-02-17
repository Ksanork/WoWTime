import sys
from GUI.MainWindow import MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from src.constants import *


class WoWIcon(QDialog):
   # __mw = None     #referecnja do głównego okna (MainWindow)

    DIALOG_MARGIN = 50            #margines okna
    ICON_MARGIN = 0               #margines ikony od okna

    __posX = None
    __posY = None
    __isPressed = None


    def __init__(self, parent=None):
        super(WoWIcon, self).__init__(parent)

        icon = QLabel()
        pixmap = QPixmap(WOW_TAKEN_IMAGE)          # <---- Do stałych
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        icon.setPixmap(pixmap)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(pixmap.width() + self.DIALOG_MARGIN, pixmap.height() + self.DIALOG_MARGIN)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        #self.setGeometry(100, 100, 100, 100)
        layout.addWidget(icon)
        self.setLayout(layout)

        self.setOnRightBottomCorner()
        self.setCursor(Qt.OpenHandCursor)

        #icon.show()
        print("konstrukt")

    def setOnRightBottomCorner(self):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()

        print(self.width())
        print(self.height())

        self.__posX = width - self.width() - self.ICON_MARGIN
        self.__posY = height - self.height() - self.ICON_MARGIN

        self.setGeometry(self.__posX, self.__posY,
                         self.width(), self.height())

    def mouseDoubleClickEvent(self, QMouseEvent):
        if not self.parent().isVisible():
            self.fadeOut()
            self.parent().show()
            #self.hide()


    def fadeOut(self):
        try:
            self.anim = QPropertyAnimation(self, "windowOpacity".encode())
            self.anim.setDuration(WOWICON_FADE_DURATION)
            self.anim.setStartValue(1.0)
            self.anim.setEndValue(0.0)
            #self.anim.finished.connect(self.finished)
            #self.anim.setEasingCurve(QEasingCurve.OutExpo)

            self.anim.start()
        except:
            print(sys.exc_info())

    def fadeIn(self):
        self.anim = QPropertyAnimation(self, "windowOpacity".encode())
        self.anim.setDuration(WOWICON_FADE_DURATION)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        # self.anim.finished.connect(self.finished)
        # self.anim.setEasingCurve(QEasingCurve.OutExpo)

        self.anim.start()

    def mousePressEvent(self, QMouseEvent):
        self.__posX = QMouseEvent.pos().x()
        self.__posY = QMouseEvent.pos().y()
        self.__isPressed = True
        self.setCursor(Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, QMouseEvent):
        self.__isPressed = None
        self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, QMouseEvent):
        if self.__isPressed:
            self.setGeometry(self.mapToGlobal(QMouseEvent.pos()).x() - self.__posX,
                             self.mapToGlobal(QMouseEvent.pos()).y() - self.__posY,
                             self.width(), self.height())
