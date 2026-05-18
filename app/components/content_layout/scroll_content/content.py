from PySide6.QtWidgets import QWidget, QGridLayout
from ..movie_container.content_container import Container
from model.reco_model import get_hybrid_recommendations
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhM2MzOGVlNTU4MjlkMjgxNWZlMGRlMWM4ZjZmM2Y4MiIsIm5iZiI6MTc3Nzg4ODUzMi4yMzIsInN1YiI6IjY5Zjg2ZDE0NWY3MTlkM2E4NzMyNmZjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4mcKyfjc5pBQ-GJSnLtIQC0dP02ELQTfqAWTObDW7bY",
}


def fetch_movies():
    movies = []

    for page in range(1, 36):
        url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            movies.extend(data.get("results", []))

    uniqueMovies = {movie["id"]: movie for movie in movies}

    return list(uniqueMovies.values())


def fetch_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        genres_list = response.json().get("genres", [])

        return {genre["name"]: genre["id"] for genre in genres_list}

    return {}


MOVIE_CACHE = fetch_movies()
GENRES_CACHE = fetch_genres()


def get_filter_options(movies):

    years = set()

    for movie in movies:
        date = movie.get("release_date")

        if date:
            years.add(date.split("-")[0])

    return sorted(list(GENRES_CACHE.keys())), sorted(list(years), reverse=True)


class Content(QWidget):
    def __init__(self, parent=None):
        super(Content, self).__init__(parent)

        self.contentLayout = QGridLayout(self)
        self.columns = 3
        self.selected_ids = set()

        sampleMovies = MOVIE_CACHE[:30]
        self.genre_id_to_name = {v: k for k, v in GENRES_CACHE.items()}

        self.display_movies(sampleMovies)

    # CONTENT
    def display_movies(self, movies):
        for index, item in enumerate(movies):
            movieName = item.get("title") or item.get("name")
            movieOverview = item.get("overview")

            if movieOverview and len(movieOverview) > 200:
                movieOverview = movieOverview[:197] + "..."
            else:
                movieOverview = movieOverview or "No description"

            moviePoster = item.get("poster_path")

            if moviePoster:
                fullPoster = f"https://image.tmdb.org/t/p/w500{moviePoster}"
            else:
                fullPoster = None

            container = Container(
                title=movieName, description=movieOverview, img=fullPoster
            )

            container.container_button.toggled.connect(
                lambda checked, mid=item.get("id"): self.handle_selection(mid, checked)
            )

            row = index // self.columns
            col = index % self.columns

            self.contentLayout.addWidget(container, row, col)

        self.contentLayout.setSpacing(15)
        self.contentLayout.setContentsMargins(20, 20, 20, 20)

    def update_movies(self, movies):

        while self.contentLayout.count():
            item = self.contentLayout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.display_movies(movies)

    def handle_selection(self, movie_id, is_checked):
        if is_checked:
            self.selected_ids.add(movie_id)
        else:
            self.selected_ids.discard(movie_id)

    def get_recommendations_ui(self):
        if not self.selected_ids:
            print("Selecteaza macar un film")
            return

        recommend = get_hybrid_recommendations(
            list(self.selected_ids), MOVIE_CACHE, self.genre_id_to_name
        )

        self.update_movies(recommend)
