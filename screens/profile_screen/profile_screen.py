from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be
from selene.support.shared.jquery_style import s


class ProfileScreen:
    """Класс для работы с экраном профиля"""

    def __init__(self):
        """Инициализация элементов экрана профиля"""
        self.avatar_image = (AppiumBy.ID, "ru.kinopoisk:id/profile_avatar_image_view")
        self.login_button = (AppiumBy.ID, "ru.kinopoisk:id/log_in_button")
        self.promo_gift_button = (AppiumBy.ID, "ru.kinopoisk:id/gift_button")
        self.settings_button = (AppiumBy.ID, "ru.kinopoisk:id/settings_button")
        self.support_button = (AppiumBy.ID, "ru.kinopoisk:id/support_button")
        self.about_app_button = (AppiumBy.ID, "ru.kinopoisk:id/about_button")
        self.make_tester_button = (AppiumBy.ID, "ru.kinopoisk:id/testing_menu_layout")
        # Элементы подстраницы 'Настройки'
        self.back_button = (
            AppiumBy.XPATH,
            "//android.view.View[@content-desc='Назад']",
        )
        self.system_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/system_theme_button")
        self.dark_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/dark_theme_button")
        self.light_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/light_theme_button")

    @step("Проверяем что экран отображается и отображается аватар пользователя")
    def profile_screen_is_opened(self) -> "ProfileScreen":
        s(self.avatar_image).should(EC.by_and(be.visible))
        return self

    @step("Нажимаем на кнопку 'Войти'")
    def tap_login_button(self) -> "ProfileScreen":
        s(self.login_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Ввести промокод'")
    def tap_promo_gift_button(self) -> "ProfileScreen":
        s(self.promo_gift_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Настройки'")
    def tap_settings_button(self) -> "ProfileScreen":
        s(self.settings_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Поддержка'")
    def tap_support_button(self) -> "ProfileScreen":
        s(self.support_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'О приложении'")
    def tap_about_app_button(self) -> "ProfileScreen":
        s(self.about_app_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Стать тестировщиком'")
    def tap_make_tester(self) -> "ProfileScreen":
        s(self.make_tester_button).should(EC.by_and(be.clickable)).click()
        return self
