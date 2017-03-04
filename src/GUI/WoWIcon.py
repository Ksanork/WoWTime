import sys

from PyQt5.QtWidgets import QDesktopWidget

from src.GUI.PrettyWidgets.DragDialog import DragDialog
from src.GUI.StatusDialog import StatusDialog
from src.GUI.TooltipDialog.TooltipDialog import TooltipDialog
from src.GUI.TooltipDialog.TooltipDialogCaller import TooltipDialogCaller


class WoWIcon(DragDialog, TooltipDialogCaller):
    ICON_MARGIN = 100

    def __init__(self, parent=None, img=None):
        try:
            super().__init__(parent, img)
            print("nowy, lepszy WoWIcon")
            self.setOnRightBottomCorner()

            tooltipDialog = StatusDialog(self, 100, 100)
            # tooltipDialog.setCaller(self)
            self.setTooltipDialog(tooltipDialog)
            # self.setEnableTooltip(None)
            self.setTransparent()

            # self.insta


        except:
            print(sys.exc_info())

    def enterEvent(self, event):
        try:
            # super().enterEvent(event)
            DragDialog.enterEvent(self, event)
            TooltipDialogCaller.enterEvent(self, event)
        except:
            print(sys.exc_info())

    def mouseMoveEvent(self, event):
        try:
            # super().enterEvent(event)
            DragDialog.mouseMoveEvent(self, event)
            TooltipDialogCaller.mouseMoveEvent(self, event)
        except:
            print(sys.exc_info())

    def setOnRightBottomCorner(self):
        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()

        self.__posX = width - self.width() - self.ICON_MARGIN
        self.__posY = height - self.height() - self.ICON_MARGIN

        print(self.__posX)
        print(self.__posY)

        self.setGeometry(self.__posX, self.__posY,
                         self.width(), self.height())

    def mouseDoubleClickEvent(self, *args, **kwargs):
        # self.fadeOut()
        pass
