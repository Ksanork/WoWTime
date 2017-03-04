from PyQt5.QtCore import QObject
from PyQt5.QtCore import QTimer

# pokazuje TooltipDialog po najechaniu myszy
# do działania wymagane jest dziedziczenie tej klasy przez Widget
# Widget musi wywołać metodę 'setTooltipDialog', gdzie argumentem jest obiekt klasy TooltipDialog
# klasa przeciąża zdarzenia myszy

class TooltipDialogCaller:
    __hideStatusTimer = None  # timer - po upływie czasu ukryj TooltipDialog
    __showStatusTimer = None  # timer - po upływie czasu pokaż TooltipDialog

    __tooltipDialog = None    # obiekt klasy TooltipDialog

    SHOW_STATUSDIALOG_TIME = 200
    HIDE_STATUSDIALOG_TIME = 400

    __enableTooltip = True

    def __init__(self):
        # QObject.__init__()
        self.__hideStatusTimer = QTimer(self)
        self.__hideStatusTimer.timeout.connect(self.hideTooltipDialog)

        self.__showStatusTimer = QTimer(self)
        self.__showStatusTimer.timeout.connect(self.showTooltipDialog)

    def setTooltipDialog(self, td):
        self.__tooltipDialog = td
        self.__tooltipDialog.setCaller(self)

    def setEnableTooltip(self, flag):
        self.__enableTooltip = flag

    def mouseMoveEvent(self, QMouseEvent):
        self.__showStatusTimer.stop()
        self.hideTooltipDialog()
        print("move")
        # self.__tooltipDialog.setPostion()

    def enterEvent(self, event):
        if not self.__showStatusTimer.isActive() and not self.__tooltipDialog.isVisible():
            self.__showStatusTimer.start(self.SHOW_STATUSDIALOG_TIME)
        self.__hideStatusTimer.stop()

        print("enter2")

    def leaveEvent(self, event):
        if not self.__hideStatusTimer.isActive():
            self.startHideTimer()
        self.__showStatusTimer.stop()

    def showTooltipDialog(self):
        if not self.__tooltipDialog.isVisible() and self.__enableTooltip:
            self.__tooltipDialog.show()

        self.__showStatusTimer.stop()
        self.__hideStatusTimer.stop()

    def hideTooltipDialog(self):
        if self.__tooltipDialog.isVisible():
            self.__tooltipDialog.hide()

        self.__showStatusTimer.stop()
        self.__hideStatusTimer.stop()

    def stopHideTimer(self):
        self.__hideStatusTimer.stop()

    def startHideTimer(self):
        self.__hideStatusTimer.start(self.HIDE_STATUSDIALOG_TIME)

