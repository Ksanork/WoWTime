from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget

from src.constants import STATUSDIALOG_MARGIN_LEFT, STATUSDIALOG_HEIGHT, STATUSDIALOG_MARGIN_BOTTOM, STATUSDIALOG_WIDTH

#przeciwdziałać jeśli okno wychodzi poza ekran
class StatusDialog(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)


    def updatePosition(self, x, y):
        self.setGeometry(x - STATUSDIALOG_MARGIN_LEFT,
                         y - STATUSDIALOG_HEIGHT - STATUSDIALOG_MARGIN_BOTTOM,
                         STATUSDIALOG_WIDTH, STATUSDIALOG_HEIGHT)

    def show(self):
        QWidget.show(self)

        # print("show")

    def enterEvent(self, event):
        self.parent().stopHideTimer()

    def leaveEvent(self, event):
        self.parent().startHideTimer()