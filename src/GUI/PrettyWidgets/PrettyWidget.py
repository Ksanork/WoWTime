import sys
from PyQt5 import QtCore

from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QWidget


class PrettyWidget(QWidget):

    __fade_duration = 1000
    __anim = None

    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            self.__anim = QPropertyAnimation(self, "windowOpacity".encode())

        except:
            print(sys.exc_info())

    def setPosition(self, x, y):
        self.setGeometry(x, y, self.width(), self.height())

    def setFadeDuration(self, duration):
        self.__fade_duration = duration

    def setTransparent(self):
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        # self.setFixedSize(self.width() + self.DIALOG_MARGIN, self.height() + self.DIALOG_MARGIN)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def fadeOut(self):
        try:
            self.__anim.setDuration(self.__fade_duration)
            self.__anim.setStartValue(1.0)
            self.__anim.setEndValue(0.0)
            # self.anim.finished.connect(self.finished)
            # self.anim.setEasingCurve(QEasingCurve.OutExpo)

            self.__anim.start()
        except:
            print(sys.exc_info())

    def fadeIn(self):
        self.__anim = QPropertyAnimation(self, "windowOpacity".encode())
        self.__anim.setDuration(self.__fade_duration)
        self.__anim.setStartValue(0.0)
        self.__anim.setEndValue(1.0)
        # self.anim.finished.connect(self.finished)
        # self.anim.setEasingCurve(QEasingCurve.OutExpo)

        self.__anim.start()