from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Приветсвенный экран с промо",
    feature="Пропуск промо"
)
class TestSkippedWelcomePromo:
    @allure_mid_level_marks(
        story="STORY-1 Приветсвенный экран",
        testcase_id="CASE-1",
        title="Пропуск промо прокликиванием кнопки 'Далее' и пропуском ЯндексПлюс",
        label="UI",
        owner="AQA FALIN PAVEL"
    )
    def test_skipped_welcome_promo_and_yandex_plus_by_tapping(self):
        kinopoisk_app.welcome_screen \
            .check_title_is_present() \
            .tap_button_next() \
            .check_title_is_present() \
            .tap_button_next() \
            .tap_yandex_plus_not_now_button() \
            .tap_allow_notifications_button()

    @allure_mid_level_marks(
        story="STORY-1 Приветсвенный экран",
        testcase_id="CASE-2",
        title="Пропуск промо свайпами вправо и пропуском ЯндексПлюс",
        label="UI",
        owner="AQA FALIN PAVEL"
    )
    def test_skipped_welcome_promo_and_yandex_plus_by_swipe(self):
        kinopoisk_app.welcome_screen.check_title_is_present()
        kinopoisk_app.device_action.swipe_left()
        kinopoisk_app.welcome_screen.check_title_is_present()
        kinopoisk_app.device_action.swipe_left()
        kinopoisk_app.welcome_screen \
            .tap_yandex_plus_not_now_button() \
            .tap_allow_notifications_button()

