from enum import Enum

IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/'
MOVIE_BASE_URL = 'https://www.themoviedb.org/movie/'
TV_SHOW_BASE_URL = 'https://www.themoviedb.org/tv/'
PERSON_BASE_URL = 'https://www.themoviedb.org/person/'


class PosterSize(Enum):
    W92 = 'w92'
    W154 = 'w154'
    W185 = 'w185'
    W342 = 'w342'
    W500 = 'w500'
    W780 = 'w780'
    ORIGINAL = 'original'
