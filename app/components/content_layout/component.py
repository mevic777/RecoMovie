from PySide6.QtWidgets import QHBoxLayout
from .scroll_filter.scroll import ScrollFilter
from .scroll_content.scroll import ScrollContent


class ContentLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super(ContentLayout, self).__init__(parent)

        self.scrollFilter = ScrollFilter()
        self.scrollContent = ScrollContent()

        self.scrollFilter.filterWidget.movieFiler.connect(
            self.scrollContent.contentWidget.update_movies
        )

        self.addWidget(self.scrollFilter, 1)
        self.addWidget(self.scrollContent, 2)
