from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared.jquery_style import s


class WelcomeScreen:
    def __init__(self):
        self.button_next = (AppiumBy.ID, "ru.kinopoisk:id/button_next")

    @step("Нажимаем на стрелку вправо что бы пропустить")
    def tap_button_next(self):
        s(self.button_next).click()
        return self
    