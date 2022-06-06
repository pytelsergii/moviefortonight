from model.movie import Movie
from model.services.themoviedb_service.configuration import IMAGE_BASE_URL, PosterSize
from model.services.themoviedb_service.genres import movie_genres


class MovieResponse:
    def __init__(self, page, results, total_results, total_pages):
        self.page = page
        self._results = results
        self.total_results = total_results
        self.total_pages = total_pages

    @property
    def results(self):
        movies = []
        for result in self._results:
            current_movie = Movie.from_dict(result)
            poster_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{current_movie.poster_path}' if current_movie.poster_path else None
            current_movie.poster_path = poster_url
            print(current_movie.poster_path)
            current_movie.genres = []
            genres = []
            for genre_id in result['genre_ids']:
                if genre_id in movie_genres:
                    genres.append(movie_genres[genre_id])
            print(genres)
            current_movie.genres = genres
            movies.append(current_movie)
        return movies

    @classmethod
    def from_dict(cls, response_dict):
        return cls(
            page=response_dict['page'],
            results=response_dict['results'],
            total_results=response_dict['total_results'],
            total_pages=response_dict['total_pages']
        )
