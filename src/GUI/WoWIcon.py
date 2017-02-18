import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from src.GUI.StatusDialog import StatusDialog
from src.constants import *

class WoWIcon(QDialog):

    DIALOG_MARGIN = 50            #margines okna
    ICON_MARGIN = 0               #margines ikony od okna

    __posX = None
    __posY = None
    __statusDialog = None

    __hideStatusTimer = None      #timer - po upływie czasu ukryj StatusDialog
    __showStatusTimer = None      #timer - po upływie czasu pokaż StatusDialog


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

        self.__statusDialog = StatusDialog(self)
        self.__statusDialog.updatePosition(self.__posX, self.__posY)


        self.__hideStatusTimer = QTimer(self)
        self.__hideStatusTimer.timeout.connect(self.hideStatusDialog)

        self.__showStatusTimer = QTimer(self)
        self.__showStatusTimer.timeout.connect(self.showStatusDialog)

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

        if self.__statusDialog.isVisible():
            self.__statusDialog.hide()
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
        # self.__isPressed = None
        self.setCursor(Qt.OpenHandCursor)

        self.__statusDialog.updatePosition(self.mapToGlobal(QMouseEvent.pos()).x() - self.__posX,
                                           self.mapToGlobal(QMouseEvent.pos()).y() - self.__posY)

        #if not self.__statusDialog.isVisible():
        #self.__showStatusTimer.start(SHOW_STATUSDIALOG_TIME)


    def mouseMoveEvent(self, QMouseEvent):
        self.__showStatusTimer.stop()
        self.hideStatusDialog()

        self.setGeometry(self.mapToGlobal(QMouseEvent.pos()).x() - self.__posX,
                         self.mapToGlobal(QMouseEvent.pos()).y() - self.__posY,
                         self.width(), self.height())




    def enterEvent(self, event):
        if not self.__showStatusTimer.isActive() and not self.__statusDialog.isVisible():
            self.__showStatusTimer.start(SHOW_STATUSDIALOG_TIME)
        self.__hideStatusTimer.stop()

    def leaveEvent(self, event):
        if not self.__hideStatusTimer.isActive():
            self.startHideTimer()
        self.__showStatusTimer.stop()

    def showStatusDialog(self):
        if not self.__statusDialog.isVisible():
            self.__statusDialog.show()

        self.__showStatusTimer.stop()
        self.__hideStatusTimer.stop()

    def hideStatusDialog(self):
        # print("hide")
        if self.__statusDialog.isVisible():
            self.__statusDialog.hide()

        self.__showStatusTimer.stop()
        self.__hideStatusTimer.stop()

    def stopHideTimer(self):
        self.__hideStatusTimer.stop()

    def startHideTimer(self):
        self.__hideStatusTimer.start(HIDE_STATUSDIALOG_TIME)