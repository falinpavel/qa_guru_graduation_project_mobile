import pytest

from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)


@allure_high_level_marks(
    epic="Экран медиа", feature="Приложение при отсутствии подключения к интернету"
)
class TestMediaScreenInTheAbsenceOfNetwork:
    @allure_mid_level_marks(
        story="STORY-3 Экран медиа",
        testcase_id="CASE-4",
        title="Поведение экрана медиа при отсутствии подключения к интернету",
        label="UI",
        owner="AQA FALIN PAVEL",
    )
    @pytest.mark.network
    @pytest.mark.ui
    def test_media_screen_have_refresh_connection_button(
        self, skipped_welcome_screen_without_network
    ):
        kinopoisk_app.navigation_bar.tap_media_button()
        kinopoisk_app.media_screen.refresh_button_is_present()
