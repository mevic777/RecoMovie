from PySide6 import QtWidgets, QtGui

class AboutAuthWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AboutAuthWindow, self).__init__(parent)

        self.setWindowTitle("RecoMovies : About Author")
        self.setWindowIcon(QtGui.QIcon("assets/logo.png"))