from typing import List

from model.services.themoviedb_service.media_type import MediaType


class TVShow:
    def __init__(self, tv_show_id, name, overview=None, vote_average=None, first_air_date=None,
                 poster_path=None, genres=None, url=None, thumb_url=None, poster_url=None):
        self.id: int = tv_show_id
        self.name: str = name
        self.overview: str = overview
        self.vote_average: int = vote_average
        self.first_air_date: str = first_air_date
        self.poster_path: str = poster_path
        self.genres: List[str] = genres
        self.url: str = url
        self.thumb_url: str = thumb_url
        self.poster_url: str = poster_url
        self.media_type = MediaType.TV_SHOW

    @classmethod
    def from_dict(cls, tv_show_dict: dict):
        return cls(
            tv_show_id=tv_show_dict['id'],
            name=tv_show_dict['name'],
            overview=tv_show_dict['overview'] if 'overview' in tv_show_dict else None,
            vote_average=tv_show_dict['vote_average'] if 'vote_average' in tv_show_dict else None,
            first_air_date=tv_show_dict['first_air_date'] if 'first_air_date' in tv_show_dict else None,
            poster_path=tv_show_dict['poster_path'] if 'poster_path' in tv_show_dict else None,
            genres=tv_show_dict['genres'] if 'genres' in tv_show_dict else None,
            url=tv_show_dict['url'] if 'url' in tv_show_dict else None,
            thumb_url=tv_show_dict['thumb_url'] if 'thumb_url' in tv_show_dict else None,
            poster_url=tv_show_dict['poster_url'] if 'poster_url' in tv_show_dict else None
        )
