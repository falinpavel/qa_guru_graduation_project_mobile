from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import have, be
from selene.support.shared.jquery_style import s


class TopNavigation:
    def __init__(self):
        self.parent_element_top_navigation = (
            AppiumBy.ID,
            "ru.kinopoisk:id/top_navigation",
        )
        self.my_movies_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Моё кино']",
        )
        self.sport_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Спорт']")
        self.channels_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Каналы']",
        )
        self.store_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Магазин']",
        )

    @step("Проверяем что на экране отображается верхнее меню с лого")
    def check_top_navigation_is_present(self):
        s(self.parent_element_top_navigation).should(EC.by_and(be.visible))
        return self

    @step("Нажимаем на кнопку Моё кино")
    def tap_my_movies_button(self):
        s(self.my_movies_button).should(
            EC.by_and(be.clickable, have.text("Моё кино"))
        ).click()
        return self

    @step("Нажимаем на кнопку 'Спорт'")
    def tap_sport_button(self):
        s(self.sport_button).should(EC.by_and(be.clickable, have.text("Спорт"))).click()
        return self

    @step("Нажимаем на кнопку 'Каналы'")
    def tap_channels_button(self):
        s(self.channels_button).should(
            EC.by_and(be.clickable, have.text("Каналы"))
        ).click()
        return self

    @step("Нажимаем на кнопку 'Магазин'")
    def tap_store_button(self):
        s(self.store_button).should(
            EC.by_and(be.clickable, have.text("Магазин"))
        ).click()
        return self
