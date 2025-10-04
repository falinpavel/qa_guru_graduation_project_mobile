import pytest

from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app


@pytest.fixture()
def skipped_welcome_screen_without_network(disable_internet):
    disable_internet()
    kinopoisk_app.welcome_screen \
            .tap_button_next() \
            .tap_button_next() \
            .tap_yandex_plus_widget_ok_button() \
            .tap_allow_notifications_button()
