import logging

import requests

from misc import THE_MOVIE_DB_API_KEY

logger = logging.getLogger(__name__)


class TheMovieDBService:
    BASE_URL = 'https://api.themoviedb.org/3/'

    def search_movie(self, query, page=1):
        endpoint = f'{self.BASE_URL}search/movie'
        logger.info(msg=f'Start searching movies for query: "{query}" page = {page}')
        response = requests.get(url=endpoint, params={'api_key': THE_MOVIE_DB_API_KEY, 'query': query, 'page': page})
        if response.ok:
            logger.info(f'Successfully retrieved movies data for query "{query}" page = {page}')
            return response.json()
        else:
            logger.warning(f'Could not retrieve data for "{query} page = {page}" - Status code {response.status_code}')
            return None
