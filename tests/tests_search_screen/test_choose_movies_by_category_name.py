import pytest

from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)


@allure_high_level_marks(
    epic="EPIC-7 Поиск фильмов",
    feature="Поиск фильмов перебором через раздел категории"
)
class TestChooseMoviesByCategory:
    @allure_mid_level_marks(
        story="STORY-8 Категории на экране поиска",
        testcase_id="CASE-8",
        title="Проверка отображения категорий на экране поиска",
        label="UI",
        owner="AQA FALIN PAVEL"
    )
    @pytest.mark.parametrize(
        "expected_category", [
            "Фильмы", "Онлайн-кинотеатр",
            "Жанры", "Страны",
            "Годы", "Критика",
            "Сериалы", "Сборы",
            "Премии", "Направления"
        ],
        ids=[
            "Movies", "Online cinema",
            "Genres", "Countries",
            "Years", "Critics",
            "Series", "Collections",
            "Premies", "Directions"
        ]
    )
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_categories_on_search_screen_is_present_and_may_be_selected(
            self, skipped_welcome_screen, expected_category
    ):
        kinopoisk_app.navigation_bar.tap_search_button()
        kinopoisk_app.search_screen \
            .check_search_screen_is_opened() \
            .check_category_is_present(category_name=expected_category) \
            .tap_category_by_name(category_name=expected_category)
