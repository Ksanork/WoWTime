from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from src.constants import *


class MainWindow(QWidget):
    __child = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(MAINWINDOW_TITLE)

        #self.setGeometry(100, 100, 1000, 100)
        self.setGeometry(0, 0, MAINWINDOW_WIDTH, MAINWINDOW_HEIGHT)
        self.center()

        exitbutton = QPushButton(QUIT_BUTTON_LABEL, self)
        exitbutton.clicked.connect(self.handleQuitButton)
        exitbutton.setGeometry(QUIT_BUTTON_X, QUIT_BUTTON_Y, QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT)

    def handleQuitButton(self):
        QApplication.quit()

    def setChild(self, child):
        self.__child = child

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def closeEvent(self, QCloseEvent):
        self.__child.fadeIn()
        self.hide()
        QCloseEvent.ignore()
