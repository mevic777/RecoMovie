from PySide6 import QtWidgets, QtGui

class AboutAppWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AboutAppWindow, self).__init__(parent)

        self.setWindowTitle("RecoMovies : About App")
        self.setWindowIcon(QtGui.QIcon("assets/logo.png"))

