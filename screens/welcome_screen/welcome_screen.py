from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import have, be
from selene.support.shared.jquery_style import s



class WelcomeScreen:


    def __init__(self):
        self.button_next = (AppiumBy.ID, "ru.kinopoisk:id/button_next")
        self.discription_title = (AppiumBy.ACCESSIBILITY_ID, "ru.kinopoisk:id/description")
        self.yandex_plus_widget_ok_button = (AppiumBy.XPATH, "//android.widget.Button")
        self.allow_notifications_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.dont_allow_notifications_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")


    @step("Нажимаем на стрелку вправо что бы пропустить")
    def tap_button_next(self):
        s(self.button_next).should(EC.by_and(be.clickable)).click()
        return self


    @step("Проверяем что на экране отображается тайтл")
    def check_title(self, text_title):
        s(self.discription_title).should(EC.by_and(
            be.visible, have.text(text_title)))
        return self


    @step("Нажимаем на кнопку 'Отлично' в виджете ЯндексПлюс")
    def tap_yandex_plus_widget_ok_button(self):
        s(self.yandex_plus_widget_ok_button).should(EC.by_and(be.clickable)).click()
        return self


    @step("Нажимаем на кнопку 'Разрешить' в виджете нотификаций")
    def tap_allow_notifications_button(self):
        s(self.allow_notifications_button).should(EC.by_and(be.clickable)).click()
        return self


    @step("Нажимаем на кнопку 'Не разрешать' в виджете нотификаций")
    def tap_dont_allow_notifications_button(self):
        s(self.dont_allow_notifications_button).should(EC.by_and(be.clickable)).click()
        return self
