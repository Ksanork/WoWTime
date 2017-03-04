import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from src.GUI.MainWindow import MainWindow
from src.GUI.WoWIcon import WoWIcon
from src.constants import WOW_TAKEN_IMAGE

if __name__ == '__main__':
    print("Hello")

    app = QApplication(sys.argv)

    try:

        mw = MainWindow()
        img = WoWIcon(mw, WOW_TAKEN_IMAGE)
        # img = WoWIcon2(mw, QPixmap(WOW_TAKEN_IMAGE))
        # img.setPosition(100, 100)
        mw.setChild(img)
        img.show()
    except:
        print(sys.exc_info())

    #tray = WoWTray(QIcon(WOW_TAKEN_IMAGE), img)


    sys.exit(app.exec_())