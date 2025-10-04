import pytest

from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)


@allure_high_level_marks(
    epic="Главный экран",
    feature="Приложение при отсутствии подключения к интернету"
)
class TestHomeScreenInTheAbsenceOfInternet:
    @allure_mid_level_marks(
        story="STORY-2 Главный экран",
        testcase_id="CASE-3",
        title="Поведение главного экрана при отсутствии подключения к интернету",
        label="UI",
        owner="AQA FALIN PAVEL",
    )
    @pytest.mark.usefixtures("skipped_welcome_screen_without_network")
    def test_home_screen_have_refresh_connection_button(self):
        kinopoisk_app.top_navigation_home_screen.tap_sport_button()
        kinopoisk_app.home_screen.refresh_button_is_present()
        kinopoisk_app.top_navigation_home_screen.tap_channels_button()
        kinopoisk_app.home_screen.refresh_button_is_present()
        kinopoisk_app.top_navigation_home_screen.tap_store_button()
        kinopoisk_app.home_screen.refresh_button_is_present()
