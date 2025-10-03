from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import have, be
from selene.support.shared.jquery_style import s


class HomeScreen:
    """Класс для работы с экраном домашней страницы"""

    def __init__(self):
        """Инициализация элементов на экране домашней страницы"""
        self.refresh_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Обновить']",
        )
        self.im_need_a_help_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Мне нужна помощь']",
        )

    @step("Нажимаем на кнопку 'Обновить'")
    def tap_refresh_button(self) -> "HomeScreen":
        s(self.refresh_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Мне нужна помощь'")
    def tap_im_need_a_help_button(self) -> "HomeScreen":
        s(self.im_need_a_help_button).should(EC.by_and(be.clickable)).click()
        return self
