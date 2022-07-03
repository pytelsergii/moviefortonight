from abc import ABC, abstractmethod
from typing import List, Union

from model.movie import Movie
from model.person import Person
from model.tv_show import TVShow


class MoviesService(ABC):

    @abstractmethod
    def multi_search(self, *args, **kwargs) -> List[Union[Movie, TVShow, Person]]:
        raise NotImplementedError
