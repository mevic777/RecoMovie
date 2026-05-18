from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class WelcomeComponent(QVBoxLayout):
    def __init__(self, parent=None):
        super(WelcomeComponent, self).__init__(parent)

        self.welcomeTitle = QLabel("Welcome to RecoMovies 🎬")
        self.welcomeText = QLabel(
            "Discover movies you’ll actually love — personalized just for you."
        )

        self.welcomeTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcomeText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.welcomeTitle.setStyleSheet(
            "font-size: 24px; font-weight: bold; margin-bottom: 10px;"
        )
        self.welcomeText.setStyleSheet(
            "font-size: 14px; color: #B3B3B3; line-height: 1.5; margin-bottom: 10px;"
        )

        self.addWidget(self.welcomeTitle)
        self.addWidget(self.welcomeText)
