from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import have, be
from selene.support.shared.jquery_style import s


class NavigationBar:
    """Класс для работы с навигационной панелью"""

    def __init__(self):
        """Инициализация элементов навигационной панели"""
        self.home_button = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/hd")
        self.media_afisha_button = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/afisha")
        self.my_button = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/my")
        self.search_button = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/search")
        self.profile_button = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/profile")

    @step("Нажимаем на кнопку 'Главная'")
    def tap_home_button(self) -> "NavigationBar":
        s(self.home_button).should(
            EC.by_and(be.clickable, have.text("Главное"))
        ).click()
        return self

    @step("Нажимаем на кнопку 'Медиа'")
    def tap_media_button(self) -> "NavigationBar":
        s(self.media_afisha_button).should(
            EC.by_and(be.clickable, have.text("Медиа"))
        ).click()
        return self

    @step("Нажимаем на кнопку 'Моё'")
    def tap_my_button(self) -> "NavigationBar":
        s(self.my_button).should(EC.by_and(be.clickable, have.text("Моё"))).click()
        return self

    @step("Нажимаем на кнопку 'Поиск'")
    def tap_search_button(self) -> "NavigationBar":
        s(self.search_button).should(
            EC.by_and(be.clickable, have.text("Поиск"))
        ).click()
        return self

    @step("Нажимаем на кнопку 'Профиль'")
    def tap_profile_button(self) -> "NavigationBar":
        s(self.profile_button).should(
            EC.by_and(be.clickable, have.text("Профиль"))
        ).click()
        return self
