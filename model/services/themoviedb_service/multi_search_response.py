from typing import List, Union

from model.movie import Movie
from model.person import Person
from model.services.themoviedb_service.configuration import MOVIE_BASE_URL, IMAGE_BASE_URL, PosterSize
from model.services.themoviedb_service.configuration import TV_SHOW_BASE_URL, PERSON_BASE_URL
from model.services.themoviedb_service.genres import movie_genres, tv_show_genres
from model.services.themoviedb_service.media_type import MediaType
from model.tv_show import TVShow


class MultiSearchResponse:
    """
    This class represents multi search response from The Movie Database API
    Check details:
    https://developers.themoviedb.org/3/search/multi-search
    """

    def __init__(self, page, results, total_results, total_pages):
        self.page: int = page
        self._results: dict = results
        self.total_results: int = total_results
        self.total_pages: int = total_pages

    @classmethod
    def from_dict(cls, response_dict: dict):
        return cls(
            page=response_dict['page'],
            results=response_dict['results'],
            total_results=response_dict['total_results'],
            total_pages=response_dict['total_pages']
        )

    @staticmethod
    def _get_genres(result, media_type: MediaType) -> List[str]:
        genres = []
        if 'genre_ids' in result:
            for genre_id in result['genre_ids']:
                if media_type == MediaType.MOVIE:
                    if genre_id in movie_genres:
                        genres.append(movie_genres[genre_id])
                elif media_type == MediaType.TV_SHOW:
                    if genre_id in tv_show_genres:
                        genres.append(tv_show_genres[genre_id])
        return genres

    @staticmethod
    def _get_person_know_for(person: Person) -> List[Union[Movie, TVShow]]:
        known_for = []
        if person.known_for:
            for item in person.known_for:
                media_type = item['media_type']
                if media_type == MediaType.MOVIE.value:
                    known_for.append(Movie.from_dict(item))
                elif media_type == MediaType.TV_SHOW.value:
                    known_for.append(TVShow.from_dict(item))

        return known_for

    @property
    def results(self) -> List[Union[Movie, TVShow, Person]]:
        search_results = []
        for result in self._results:
            media_type = result['media_type']
            if media_type == MediaType.MOVIE.value:
                movie = Movie.from_dict(result)
                movie.url = f'{MOVIE_BASE_URL}{movie.id}'
                movie.thumb_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{movie.poster_path}' if movie.poster_path else ''
                movie.poster_url = f'{IMAGE_BASE_URL}{PosterSize.ORIGINAL.value}{movie.poster_path}' if movie.poster_path else ''
                movie.genres = self._get_genres(result, MediaType.MOVIE)
                search_results.append(movie)

            elif media_type == MediaType.TV_SHOW.value:
                tv_show = TVShow.from_dict(result)
                tv_show.url = f'{TV_SHOW_BASE_URL}{tv_show.id}'
                tv_show.thumb_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{tv_show.poster_path}' if tv_show.poster_path else ''
                tv_show.poster_url = f'{IMAGE_BASE_URL}{PosterSize.ORIGINAL.value}{tv_show.poster_path}' if tv_show.poster_path else ''
                tv_show.genres = self._get_genres(result, MediaType.TV_SHOW)
                search_results.append(tv_show)

            elif media_type == MediaType.PERSON.value:
                person = Person.from_dict(result)
                person.url = f'{PERSON_BASE_URL}{person.id}'
                person.thumb_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{person.profile_path}' if person.profile_path else ''
                person.poster_url = f'{IMAGE_BASE_URL}{PosterSize.ORIGINAL.value}{person.profile_path}' if person.profile_path else ''
                person.known_for = self._get_person_know_for(person)
                search_results.append(person)

        return search_results
