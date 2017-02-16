from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):
    __child = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Free-WoW")
        self.center()

        exitbutton = QPushButton("Zamknij", self)
        exitbutton.clicked.connect(self.handleQuitButton)
        exitbutton.setGeometry(100, 100, 50, 20)

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