from PySide6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


class SearchBar(QHBoxLayout):
    def __init__(self, parent=None):
        super(SearchBar, self).__init__(parent)

        self.lineEdit = QLineEdit(placeholderText="Search Bar")
        self.lineEdit.setMinimumHeight(40)

        self.searchButton = QPushButton("Search")
        self.searchButton.setMinimumHeight(40)

        self.addWidget(self.lineEdit)
        self.addWidget(self.searchButton)
