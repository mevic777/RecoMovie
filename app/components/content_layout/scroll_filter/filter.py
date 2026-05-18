from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QCheckBox, QPushButton
from PySide6.QtCore import Signal
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhM2MzOGVlNTU4MjlkMjgxNWZlMGRlMWM4ZjZmM2Y4MiIsIm5iZiI6MTc3Nzg4ODUzMi4yMzIsInN1YiI6IjY5Zjg2ZDE0NWY3MTlkM2E4NzMyNmZjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4mcKyfjc5pBQ-GJSnLtIQC0dP02ELQTfqAWTObDW7bY",
}


class Filter(QWidget):
    movieFiler = Signal(list)

    def __init__(self, genres, years, parent=None):
        super(Filter, self).__init__(parent)

        filterLayout = QVBoxLayout(self)

        self.all_genres = genres
        self.checked_genres = set()
        self.checked_year = set()

        self.genres_label = QLabel("<b>Genres</b>")
        filterLayout.addWidget(self.genres_label)

        for genre in self.all_genres:
            genre_cb = QCheckBox(genre)
            filterLayout.addWidget(genre_cb)

            genre_cb.toggled.connect(
                lambda checked, g=genre: self.check_genre(checked, g)
            )

        self.year_label = QLabel("<b>Year</b>")
        filterLayout.addWidget(self.year_label)

        for year in years:
            year_cb = QCheckBox(year)
            filterLayout.addWidget(year_cb)

            year_cb.toggled.connect(lambda checked, y=year: self.check_year(checked, y))

        self.filterButton = QPushButton("Apply filters")
        filterLayout.addWidget(self.filterButton)

        self.filterButton.clicked.connect(self.apply_filters)

    def check_genre(self, checked, g):
        if checked:
            self.checked_genres.add(g)
        else:
            self.checked_genres.discard(g)

        print(g)

    def check_year(self, checked, y):
        if checked:
            self.checked_year.add(y)
        else:
            self.checked_year.remove(y)

    def apply_filters(self):
        from ..scroll_content.content import GENRES_CACHE, MOVIE_CACHE

        genres_ids = [GENRES_CACHE[g] for g in self.checked_genres]
        filtered_movies = []

        for movie in MOVIE_CACHE:
            movie_year = movie.get("release_date", "").split("-")[0]
            year_match = True

            if self.checked_year:
                year_match = movie_year in self.checked_year

            movie_genres = movie.get("genre_ids", [])
            genre_match = True

            if genres_ids:
                genre_match = all(gid in movie_genres for gid in genres_ids)

            if year_match and genre_match:
                filtered_movies.append(movie)

        self.movieFiler.emit(filtered_movies[:30])
