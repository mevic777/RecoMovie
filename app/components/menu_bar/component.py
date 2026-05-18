from components.menu_bar.aboutAuth import AboutAuthWindow
from components.menu_bar.aboutApp import AboutAppWindow
from PySide6.QtWidgets import QMenuBar


class MenuComponent(QMenuBar):
    def __init__(self, parent=None):

        super(MenuComponent, self).__init__(parent)

        docMenu = self.addMenu("Documentatie")

        aboutApp = docMenu.addAction("Despre aplicatie")
        aboutAuth = docMenu.addAction("Despre autor")

        aboutApp.triggered.connect(self.openAboutAppWindow)
        aboutAuth.triggered.connect(self.openAboutAuthWindow)

    def openAboutAppWindow(self):
        self.about = AboutAppWindow()
        self.about.exec()

    def openAboutAuthWindow(self):
        self.author = AboutAuthWindow()
        self.author.exec()
