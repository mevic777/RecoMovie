from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Qt
from .filter import Filter
from ..scroll_content.content import get_filter_options, MOVIE_CACHE


class ScrollFilter(QScrollArea):
    def __init__(self, parent=None):
        super(ScrollFilter, self).__init__(parent)

        movieGenres, movieYears = get_filter_options(MOVIE_CACHE)

        self.filterWidget = Filter(genres=movieGenres, years=movieYears)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(self.filterWidget)
