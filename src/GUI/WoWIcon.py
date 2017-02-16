import sys
from GUI.MainWindow import MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget





class WoWIcon(QDialog):
   # __mw = None     #referecnja do głównego okna (MainWindow)

    DIALOG_MARGIN = 50            #margines okna
    ICON_MARGIN = 0               #margines ikony od okna

    def __init__(self, parent=None):
        super(WoWIcon, self).__init__(parent)

        icon = QLabel()
        pixmap = QPixmap("images/wow.png")          # <---- Do stałych
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

        #icon.show()
        print("konstrukt")

    def setOnRightBottomCorner(self):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()

        print(self.width())
        print(self.height())

        self.setGeometry(width - self.width() - self.ICON_MARGIN, height - self.height() - self.ICON_MARGIN,
                         self.width(), self.height())

    def mousePressEvent(self, QMouseEvent):
        if not self.parent().isVisible():
            self.fadeOut()
            self.parent().show()
            #self.hide()


    def fadeOut(self):
        try:
            self.anim = QPropertyAnimation(self, "windowOpacity".encode())
            self.anim.setDuration(300)
            self.anim.setStartValue(1.0)
            self.anim.setEndValue(0.0)
            #self.anim.finished.connect(self.finished)
            #self.anim.setEasingCurve(QEasingCurve.OutExpo)

            self.anim.start()
        except:
            print(sys.exc_info())

    def fadeIn(self):
        self.anim = QPropertyAnimation(self, "windowOpacity".encode())
        self.anim.setDuration(300)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        # self.anim.finished.connect(self.finished)
        # self.anim.setEasingCurve(QEasingCurve.OutExpo)

        self.anim.start()