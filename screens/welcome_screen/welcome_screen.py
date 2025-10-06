from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be
from selene.support.shared.jquery_style import s


class WelcomeScreen:
    """Класс для работы с экраном приветствия"""

    def __init__(self):
        """Инициализация элементов на экране приветствия"""
        self.button_next = (AppiumBy.ID, "ru.kinopoisk:id/button_next")
        self.discription_title = (
            AppiumBy.ID,
            "ru.kinopoisk:id/description",
        )
        self.yandex_plus_widget_ok_button = (
            AppiumBy.ID, "ru.kinopoisk:id/button_payment"
        )
        self.allow_notifications_button = (
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_allow_button",
        )
        self.dont_allow_notifications_button = (
            AppiumBy.ID,
            "com.android.permissioncontroller:id/permission_deny_button",
        )
        self.yandex_plus_not_now_button = (
            AppiumBy.ID,
            "ru.kinopoisk:id/button_skip_subscription",
        )
        self.yandex_plus_try_free_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Попробовать бесплатно']",
        )

    @step("Нажимаем на стрелку вправо что бы пропустить")
    def tap_button_next(self) -> "WelcomeScreen":
        s(self.button_next).should(EC.by_and(be.clickable)).click()
        return self

    @step("Проверяем что на экране отображается тайтл")
    def check_title_is_present(self) -> "WelcomeScreen":
        s(self.discription_title).should(EC.by_and(be.visible))
        return self

    @step(
        "Проверяем что при выключенном интернете отображается кнопка 'Отлично' для промо ЯндексПлюс"
    )
    def check_yandex_plus_widget_ok_button_is_present(self) -> "WelcomeScreen":
        s(self.yandex_plus_widget_ok_button).should(EC.by_and(be.visible))
        return self

    @step("Нажимаем на кнопку 'Отлично' в виджете ЯндексПлюс")
    def tap_yandex_plus_widget_ok_button(self) -> "WelcomeScreen":
        s(self.yandex_plus_widget_ok_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Не сейчас' в виджете ЯндексПлюс")
    def tap_yandex_plus_not_now_button(self) -> "WelcomeScreen":
        s(self.yandex_plus_not_now_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Попробовать бесплатно' в виджете ЯндексПлюс")
    def tap_yandex_plus_try_free_button(self) -> "WelcomeScreen":
        s(self.yandex_plus_try_free_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Разрешить' в виджете нотификаций")
    def tap_allow_notifications_button(self) -> "WelcomeScreen":
        s(self.allow_notifications_button).should(EC.by_and(be.clickable)).click()
        return self

    @step("Нажимаем на кнопку 'Не разрешать' в виджете нотификаций")
    def tap_dont_allow_notifications_button(self) -> "WelcomeScreen":
        s(self.dont_allow_notifications_button).should(EC.by_and(be.clickable)).click()
        return self
