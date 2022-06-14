from typing import Optional, List, Union

from model.movie import Movie
from model.person import Person
from model.services.movies_service_interface import MoviesService
from model.tv_show import TVShow


class MultiSearchModel:

    def __init__(self, service):
        self._service: MoviesService = service

    def get_multi_search_results(self, query: str, offset: int) -> Optional[List[Union[Movie, TVShow, Person]]]:
        return self._service.multi_search(query, page=offset)
