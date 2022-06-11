import logging

from model.movie import Movie
from model.services.themoviedb_service.configuration import MOVIE_BASE_URL
from model.services.themoviedb_service.genres import movie_genres
from model.services.themoviedb_service.movie_db_service import TheMovieDBService

logger = logging.getLogger(__name__)


class MovieSearchModel:

    def __init__(self):
        self._service = TheMovieDBService()

    @staticmethod
    def _convert_to_movie_list(results):
        movies = []
        for result in results:
            current_movie = Movie.from_dict(result)

            if not current_movie.release_year:
                if current_movie.release_date:
                    current_movie.release_year = current_movie.release_date.split('-')[0]
                else:
                    logger.debug(f'{current_movie.title} missing release_date')
                    current_movie.release_year = ''

            if not current_movie.genres:
                current_movie.genres = []
                if 'genre_ids' in result:
                    if result['genre_ids']:
                        for genre_id in result['genre_ids']:
                            if genre_id in movie_genres:
                                current_movie.genres.append(movie_genres[genre_id])
                    else:
                        logger.debug(f'{current_movie.title} {current_movie.release_year} missing genres')

            if not current_movie.url:
                current_movie.url = f'{MOVIE_BASE_URL}{current_movie.id}'

            if not current_movie.vote_average:
                current_movie.vote_average = 0
                logger.debug(f'{current_movie.title} {current_movie.release_year} missing vote_average')

            movies.append(current_movie)
        return movies

    def get_search_results(self, query, offset):
        movies = []
        response = self._service.search_movie(query, page=offset)
        if response:
            movies = self._convert_to_movie_list(response['results'])
        return movies
