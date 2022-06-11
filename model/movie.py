class Movie:
    def __init__(self, movie_id, title, overview=None, vote_average=None, release_date=None,
                 release_year=None, poster_path=None, genres=None, url=None):
        self.id = movie_id
        self.title = title
        self.overview = overview
        self.vote_average = vote_average
        self.release_date = release_date  # 2017-06-10
        self.release_year = release_year
        self.poster_path = poster_path
        self.genres = genres
        self.url = url

    @classmethod
    def from_dict(cls, movie_dict):
        return cls(
            movie_id=movie_dict['id'],
            title=movie_dict['title'],
            overview=movie_dict['overview'] if 'overview' in movie_dict else None,
            vote_average=movie_dict['vote_average'] if 'vote_average' in movie_dict else None,
            release_date=movie_dict['release_date'] if 'release_date' in movie_dict else None,
            release_year=movie_dict['release_year'] if 'release_year' in movie_dict else None,
            poster_path=movie_dict['poster_path'] if 'poster_path' in movie_dict else None,
            genres=movie_dict['genres'] if 'genres' in movie_dict else None,
            url=movie_dict['url'] if 'url' in movie_dict else None
        )
