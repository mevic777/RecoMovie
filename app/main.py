import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Qt
from components.menu_bar.component import MenuComponent
from components.search_bar.component import SearchBar
from components.welcome.component import WelcomeComponent
from components.content_layout.component import ContentLayout


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # App initialization parameters
        self.setWindowTitle("RecoMovies")
        self.setWindowIcon(QIcon("assets/logo.ico"))
        self.setMinimumSize(1200, 700)

        # FileMenu for the app
        fileMenu = MenuComponent()
        self.setMenuBar(fileMenu)

        # central widget for QMainWindow
        mainContainer = QWidget()
        self.setCentralWidget(mainContainer)

        # Main Layout
        mainLayout = QVBoxLayout(mainContainer)

        # Welcome Layout
        welcomeLayout = WelcomeComponent()

        # Search Bar
        searchBar = SearchBar()

        # Content Layout and Filter
        contentLayout = ContentLayout()

        mainLayout.addLayout(welcomeLayout)
        mainLayout.addLayout(searchBar)
        mainLayout.addLayout(contentLayout)

        getRecommendationButton = QPushButton("Recommend")
        getRecommendationButton.setObjectName("reco-btn")
        getRecommendationButton.clicked.connect(
            contentLayout.scrollContent.contentWidget.get_recommendations_ui
        )
        mainLayout.addWidget(
            getRecommendationButton, alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setStyleSheet("""
            * {
                font-family: Inter;
            }

            QWidget {
                background-color: #1A1A1A;
                color: #E5E7EB;
            }

            /* TITLURI */
            QLabel#title {
                font-size: 20px;
                font-weight: bold;
            }

            /* TEXT SECUNDAR */
            QLabel#description {
                color: #9CA3AF;
                font-size: 13px;
            }

            /* BUTTON */
            QPushButton {
                background-color: #F97316;
                color: white;
                border-radius: 8px;
                padding: 8px 12px;
                font-weight: bold;
                min-width: 90px;
            }

            QPushButton:hover {
                background-color: #FB923C;
            }

            /* INPUT */
            QLineEdit {
                background-color: #262626;
                border: 2px solid #333;
                border-radius: 8px;
                padding: 8px 12px;
                color: #E5E7EB;
            }

            QLineEdit:focus {
                border: 2px solid #F97316;
            }

            /* MENU */
            QMenuBar {
                background-color: #1A1A1A;
            }

            QMenuBar::item:selected {
                background: #262626;
            }

            QMenu {
                background-color: #262626;
                border: 1px solid #333;
                min-width: 100px;
            }

            QMenu::item:selected {
                background-color: #F97316;
            }

            /* Movie container card */ 
            QWidget#card {
                background-color: #262626;
                border-radius: 12px;
                padding: 10px;
            }

            QWidget#card:hover {
                border: 1px solid #F97316;
            }
                           
            QLabel#cardTitle {
                font-size: 16px;
                font-weight: bold;
                background-color: #262626;
            }

            QLabel#cardDescription {
                color: #9CA3AF;
                font-size: 13px;
                background-color: #262626;
            }
                           
            QPushButton#container_button {
                margin-top: 10px;               
            }
                           
            QPushButton#container_button:checked {
                background: #fc6b05;
                color: black;               
            }
                           
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
                border-radius: 6px;
                border: 1px solid #d1d5db;
            }

            QCheckBox::indicator:unchecked {
                background-color: #ffffff;
                border: 1px solid #d1d5db;
            }

            QCheckBox::indicator:unchecked:hover {
                border: 1px solid #F97316;
            }

            QCheckBox::indicator:checked {
                background-color: #F97316;
                border: 1px solid #F97316;
                image: url('./assets/check.png'); 
            }
                           
            QPushButton:pressed {
                background-color: #ab4d0c;
            }
                           
            QPushButton#reco-btn {
                width: 200px;
            }
                           
           QWidget#card[selected="true"] {
                border: 2px solid #ab4d0c;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec())
