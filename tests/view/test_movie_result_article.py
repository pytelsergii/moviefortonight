from typing import Callable

import pytest

from model.movie import Movie
from view.movie_result_article import MovieResultArticle


@pytest.fixture(scope='module')
def movie_result_article() -> Callable:
    def wrapper(movie: Movie):
        return MovieResultArticle(movie)

    return wrapper


@pytest.mark.parametrize(
    "movie, expected_title",
    [pytest.param(Movie(123, 'Movie 1', release_date='2012-09-08'), 'Movie 1 (2012)', id="Movie with release year"),
     pytest.param(Movie(124, 'Movie 2'), 'Movie 2', id="Movie without release year")]
)
def test_title_formatted_correctly(movie_result_article, movie, expected_title) -> None:
    result_article = movie_result_article(movie)
    assert result_article.title == expected_title, 'Title is incorrect'


@pytest.mark.parametrize(
    "movie, expected_description",
    [pytest.param(Movie(123, 'Movie 1', vote_average=6.9, genres=['Action']), '⭐ 6.9  Movie\nAction',
                  id="Movie vote_average and genres are available"),
     pytest.param(Movie(124, 'Movie 2', vote_average=5), '⭐ 5  Movie\n', id="Movie only vote_average_available"),
     pytest.param(Movie(124, 'Movie 2'), 'No ratings  Movie\n', id="Movie no vote_average no genres"),
     pytest.param(Movie(124, 'Movie 2', genres=['Action']), 'No ratings  Movie\nAction',
                  id="Movie genres are available no vote_average")]
)
def test_description_formatted_correctly(movie_result_article, movie, expected_description):
    result_article = movie_result_article(movie)
    assert result_article.description == expected_description, 'Description is incorrect'


input_message_data = [
    (Movie(123, 'Movie 1', vote_average=6.9, genres=['Action', 'Drama'], overview='Some overview',
           release_date='2012-09-08', poster_url='https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg'),
     '<b>Movie 1 (2012)</b>\n'
     'Action, Drama\n'
     '<b>⭐</b> 6.9\n'
     'Some overview'
     '<a href="https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg">&#8205;</a>'),
    (Movie(124, 'Movie 2', genres=['Action'], overview='Some overview', release_date='2012-09-08',
           poster_url='https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg'),
     '<b>Movie 2 (2012)</b>\n'
     'Action\n'
     'No ratings\n'
     'Some overview'
     '<a href="https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg">&#8205;</a>'),
    (Movie(125, 'Movie 3', genres=['Action'], release_date='2012-09-08',
           poster_url='https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg'),
     '<b>Movie 3 (2012)</b>\n'
     'Action\n'
     'No ratings'
     '<a href="https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg">&#8205;</a>'),
    (Movie(126, 'Movie 4', release_date='2012-09-08',
           poster_url='https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg'),
     '<b>Movie 4 (2012)</b>\n'
     'No ratings'
     '<a href="https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg">&#8205;</a>')
]


@pytest.mark.parametrize("movie, expected_input_message", input_message_data,
                         ids=['All movie data available', 'No vote average', 'No overview', 'No genres'])
def test_input_message_content_formatted_correctly(movie_result_article, movie, expected_input_message) -> None:
    result_article = movie_result_article(movie)
    assert result_article.input_message_content.message_text == expected_input_message, 'Incorrect input message'


@pytest.mark.parametrize(
    "movie, expected_url",
    [pytest.param(Movie(123, 'Movie 1', thumb_url='https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg'),
                  'https://image.tmdb.org/t/p/w92//ilrZAV2klTB0FLxLb01bOp5pzD9.jpg', id="Thumb url available"),
     pytest.param(Movie(124, 'Movie 2'), MovieResultArticle.THUMB_PLACEHOLDER,
                  id="No thumb url, placeholder should be used")]
)
def test_thumb_url(movie_result_article, movie, expected_url) -> None:
    result_article = movie_result_article(movie)
    assert result_article.thumb_url == expected_url, 'Incorrect thumb url'
