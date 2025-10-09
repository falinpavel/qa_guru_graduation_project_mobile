import pytest

from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)


@allure_high_level_marks(
    epic="EPIC-7 Поиск фильмов",
    feature="Поиск фильмов и поисковая выдача"
)
class TestSearchMoviesAndCheckResults:
    @allure_mid_level_marks(
        story="STORY-7 Поиск фильмов",
        testcase_id="CASE-7",
        title="Проверка точности поисковый выдачи в зависимости от введенного запроса",
        label="UI", owner="AQA FALIN PAVEL"
    )
    @pytest.mark.parametrize(
        "movie_name", [
            "Властелин колец: Братство кольца",
            "Хоббит: Нежданное путешествие",
            "Дюна",
            "Добро пожаловать в Zомбилэнд",
            "Остаться в живых"
        ],
        ids=[
            "The Lord of the Rings: The Fellowship of the Ring",
            "The Hobbit: An Unexpected Journey",
            "Dune: Part One",
            "Zombieland",
            "Lost"
        ]
    )
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_type_movies_name_and_check_search_results(
            self, skipped_welcome_screen, movie_name
    ):
        kinopoisk_app.navigation_bar.tap_search_button()
        kinopoisk_app.search_screen \
            .check_search_screen_is_opened() \
            .click_search_input_and_type_of_value(to_search=movie_name) \
            .check_first_search_result(expected_result=movie_name)
