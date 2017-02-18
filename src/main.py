import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QWidget

from src.GUI.MainWindow import MainWindow
from src.GUI.WoWIcon import WoWIcon
from src.GUI.WoWTray import WoWTray
from src.constants import WOW_TAKEN_IMAGE

if __name__ == '__main__':
    print("Hello")

    app = QApplication(sys.argv)


    mw = MainWindow()
    img = WoWIcon(mw)
    mw.setChild(img)
    img.show()

    #tray = WoWTray(QIcon(WOW_TAKEN_IMAGE), img)


    sys.exit(app.exec_())