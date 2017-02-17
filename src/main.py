import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget

from src.GUI.MainWindow import MainWindow
from src.GUI.WoWIcon import WoWIcon

if __name__ == '__main__':
    print("Hello")

    app = QApplication(sys.argv)

    mw = MainWindow()
    img = WoWIcon(mw)
    mw.setChild(img)
    img.show()

    sys.exit(app.exec_())