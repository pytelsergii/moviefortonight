import requests

from misc import THE_MOVIE_DB_API_KEY
from model.services.themoviedb_service.movie_response import MovieResponse


def search_movie(query):
    endpoint_url = f'https://api.themoviedb.org/3/search/movie?api_key={THE_MOVIE_DB_API_KEY}&language=en-US&query={query}&page=1'
    response = requests.get(url=endpoint_url)
    return MovieResponse.from_dict(response.json()) if response.ok else None
