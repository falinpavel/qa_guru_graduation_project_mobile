from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be
from selene.support.shared.jquery_style import s


class SettingsScreen:
    """Класс для работы с дочерним экраном настроек"""
    def __init__(self):
        """Инициализация элементов экрана настроек"""
        self.back_button = (
            AppiumBy.XPATH,
            "//android.view.View[@content-desc='Назад']",
        )
        self.system_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/system_theme_button")
        self.dark_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/dark_theme_button")
        self.light_theme_button = (AppiumBy.ID, "ru.kinopoisk:id/light_theme_button")

    @step("Меняем тему на 'Системная' и проверяем изменение")
    def tap_system_theme_button(self) -> "SettingsScreen":
        s(self.system_theme_button).should(EC.by_and(be.clickable)).click().should(be.enabled)
        return self

    @step("Меняем тему на 'Тёмная' и проверяем изменение")
    def tap_dark_theme_button(self) -> "SettingsScreen":
        s(self.dark_theme_button).should(EC.by_and(be.clickable)).click().should(be.enabled)
        return self

    @step("Меняем тему на 'Светлая' и проверяем изменение")
    def tap_light_theme_button(self) -> "SettingsScreen":
        s(self.light_theme_button).should(EC.by_and(be.clickable)).click().should(be.enabled)
        return self

    @step("Возвращаемся на экран профиля")
    def tap_back_button(self) -> "ProfileScreen":
        s(self.back_button).should(EC.by_and(be.clickable)).click()
        return self
