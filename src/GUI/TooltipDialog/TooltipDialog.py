import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget

from src.GUI.PrettyWidgets.PrettyWidget import PrettyWidget


class TooltipDialog(QDialog, PrettyWidget):

    __caller = None     # obiekt klasy TooltipDialogCaller
    __tooltipMargin = 0

    def __init__(self, parent=None, width=None, height=None):
        QWidget.__init__(self, parent)

        if width and height:
            self.setFixedSize(width, height)

    # dodać marginesy
    # def updatePosition(self, x, y):
    #     self.setGeometry(x, y - self.height() - self.__tooltipMargin, self.width(), self.height())

    # metoda wywoływane jest przez TooltipDialogCaller
    def setCaller(self, caller):
        self.__caller = caller;

    def enterEvent(self, event):
        if self.__caller:
            self.__caller.stopHideTimer()

    def leaveEvent(self, event):
        if self.__caller:
            self.__caller.startHideTimer()

    def show(self):
        super().show()
        try:
            if self.__caller:
                self.setPosition(self.__caller.pos().x() - self.width()/2.6,        # ?????
                                 self.__caller.pos().y() - self.height() - self.__tooltipMargin)
        except:
            print(sys.exc_info())