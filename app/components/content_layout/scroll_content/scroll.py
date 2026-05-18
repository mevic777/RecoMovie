from PySide6.QtWidgets import QScrollArea
from .content import Content


class ScrollContent(QScrollArea):
    def __init__(self, parent=None):
        super(ScrollContent, self).__init__(parent)

        self.contentWidget = Content()
        self.setWidgetResizable(True)
        self.setWidget(self.contentWidget)
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
