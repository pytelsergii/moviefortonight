from typing import List

from model.services.themoviedb_service.media_type import MediaType


class Movie:
    def __init__(self, movie_id, title, overview=None, vote_average=None, release_date=None,
                 poster_path=None, genres=None, url=None, thumb_url=None, poster_url=None):
        self.id: int = movie_id
        self.title: str = title
        self.overview: str = overview
        self.vote_average: int = vote_average
        self.release_date: str = release_date
        self.poster_path: str = poster_path
        self.genres: List[str] = genres
        self.url: str = url
        self.thumb_url: str = thumb_url
        self.poster_url: str = poster_url
        self.media_type = MediaType.MOVIE

    @classmethod
    def from_dict(cls, movie_dict: dict):
        return cls(
            movie_id=movie_dict['id'],
            title=movie_dict['title'],
            overview=movie_dict['overview'] if 'overview' in movie_dict else None,
            vote_average=movie_dict['vote_average'] if 'vote_average' in movie_dict else None,
            release_date=movie_dict['release_date'] if 'release_date' in movie_dict else None,
            poster_path=movie_dict['poster_path'] if 'poster_path' in movie_dict else None,
            genres=movie_dict['genres'] if 'genres' in movie_dict else None,
            url=movie_dict['url'] if 'url' in movie_dict else None,
            thumb_url=movie_dict['thumb_url'] if 'thumb_url' in movie_dict else None,
            poster_url=movie_dict['poster_url'] if 'poster_url' in movie_dict else None
        )
