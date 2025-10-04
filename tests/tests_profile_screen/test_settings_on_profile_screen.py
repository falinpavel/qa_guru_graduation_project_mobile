from helpers.mobile_application_manager.mobile_application_manager import kinopoisk_app
from utils.allure.allure_custom_labels import (
    allure_high_level_marks,
    allure_mid_level_marks,
)


@allure_high_level_marks(
    epic="Профиль пользователя", feature="Настройки приложения в профиле пользователя"
)
class TestSettingsOnProfileScreen:
    @allure_mid_level_marks(
        story="STORY-4 Профиль",
        testcase_id="CASE-5",
        title="Проверка отображения настроек приложения в профиле пользователя",
        label="UI",
        owner="AQA FALIN PAVEL",
    )
    def test_in_settings_on_profile_screen_can_edit_theme(self, skipped_welcome_screen):
        kinopoisk_app.navigation_bar.tap_profile_button()
        kinopoisk_app.profile_screen \
            .profile_screen_is_opened() \
            .tap_settings_button()
        kinopoisk_app.settings_screen \
            .tap_dark_theme_button() \
            .tap_light_theme_button() \
            .tap_system_theme_button()
