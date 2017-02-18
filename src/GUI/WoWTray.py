import sys
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QWidget


class WoWTray(QSystemTrayIcon):
    __wowIcon = None

    def __init__(self, icon, mw):
        QSystemTrayIcon.__init__(self, icon)

        self.__wowIcon = mw

        #self.showMessage('Witaj', 'WoWTime aktywny')

        contextMenu = QMenu()
        actionOpenMW = contextMenu.addAction("Otwórz")
        actionOpenMW.triggered.connect(self.open)
        self.setContextMenu(contextMenu)

        self.activated.connect(self.trayActivated)

        self.show()

    def trayActivated(self, reason):
        print(reason)

        try:
            if reason == 2:
                if not self.__wowIcon.parent().isVisible():
                    self.__wowIcon.parent().show()
                    self.__wowIcon.fadeOut()
        except:
            print(sys.exc_info())

    def open(self):
        print("open")