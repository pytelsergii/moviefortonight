import logging
from typing import List, Union, Optional

import requests

from misc import THE_MOVIE_DB_API_KEY
from model.movie import Movie
from model.person import Person
from model.services.movies_service_interface import MoviesService
from model.services.themoviedb_service.multi_search_response import MultiSearchResponse
from model.tv_show import TVShow

logger = logging.getLogger(__name__)


class TheMovieDBService(MoviesService):
    BASE_URL = 'https://api.themoviedb.org/3/'

    def multi_search(self, query: str, page: int = 1) -> Optional[List[Union[Movie, TVShow, Person]]]:
        endpoint = f'{self.BASE_URL}search/multi'
        logger.info(msg=f'Start multi search for query: "{query}" page = {page}')
        response = requests.get(url=endpoint, params={'api_key': THE_MOVIE_DB_API_KEY, 'query': query, 'page': page})
        if response.ok:
            logger.info(f'Successfully retrieved multi search data for query "{query}" page = {page}')
            return MultiSearchResponse.from_dict(response.json()).results
        else:
            logger.warning(f'Could not retrieve data for "{query} page = {page}" - Status code {response.status_code}')
            return None
