from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath
import requests


class Container(QWidget):
    def __init__(self, title, description, img, parent=None):
        super(Container, self).__init__(parent)
        self.setObjectName("card")
        self.setAttribute(
            Qt.WA_StyledBackground, True
        )  # Permite ca widgetului sa se poate stiliza in QSS
        self.setMinimumWidth(150)

        layout_contaier = QVBoxLayout(self)

        self.container_img = QLabel()
        self.container_img.setFixedHeight(500)
        self.container_img.setScaledContents(True)
        self.container_img.setStyleSheet("background: transparent; border: none;")

        if img:
            try:
                imgData = requests.get(img).content
                poster = QPixmap()
                poster.loadFromData(imgData)

                roundedPoster = QPixmap(poster.size())
                roundedPoster.fill(Qt.transparent)

                painter = QPainter(roundedPoster)
                painter.setRenderHint(QPainter.Antialiasing)

                path = QPainterPath()
                path.addRoundedRect(0, 0, poster.width(), poster.height(), 30, 30)
                painter.setClipPath(path)

                painter.drawPixmap(0, 0, poster)
                painter.end()

                self.container_img.setPixmap(roundedPoster)
            except:
                self.container_img.setText("No image")
        else:
            self.container_img.setText("No image")

        self.container_title = QLabel(title)
        self.container_title.setFixedHeight(50)
        self.container_title.setObjectName("cardTitle")

        self.container_description = QLabel(description)
        self.container_description.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.container_description.setObjectName("cardDescription")
        self.container_description.setWordWrap(True)

        self.container_button = QPushButton("Select")
        self.container_button.setObjectName("container_button")
        self.container_button.setCheckable(True)

        self.container_button.toggled.connect(self.select_movie)

        layout_contaier.addWidget(self.container_img)
        layout_contaier.addWidget(self.container_title)
        layout_contaier.addWidget(self.container_description)
        layout_contaier.addWidget(self.container_button)

    def select_movie(self, checked):

        if checked:
            self.container_button.setIcon(QIcon("./assets/check.png"))
            self.container_button.setIconSize(QSize(14, 14))
            self.container_button.setText("Selected")
            self.setProperty("selected", checked)
            self.style().unpolish(self)
            self.style().polish(self)
        else:
            self.container_button.setIcon(QIcon())
            self.container_button.setText("Select")
            self.setProperty("selected", checked)
            self.style().unpolish(self)
            self.style().polish(self)
