from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app


class TestOpen:
    def test_open(self):
        kinopoisk_app.welcome_screen.tap_button_next()