from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget

from src.GUI.PrettyWidgets.PrettyWidget import PrettyWidget
from src.GUI.TooltipDialog.TooltipDialog import TooltipDialog
from src.status_dialog_1_ui import Ui_StatusDialog1


class StatusDialog(TooltipDialog, PrettyWidget):

    def __init__(self, parent=None, width=None, height=None):
        super().__init__(parent)

        self.ui = Ui_StatusDialog1()
        self.ui.setupUi(self)

        print(self.width())

        self.setTransparent()