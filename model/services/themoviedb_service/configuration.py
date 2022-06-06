from enum import Enum

IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/'


class PosterSize(Enum):
    W92 = 'w92'
    W154 = 'w154'
    W185 = 'w185'
    W342 = 'w342'
    W500 = 'w500'
    W780 = 'w780'
    ORIGINAL = 'original'
