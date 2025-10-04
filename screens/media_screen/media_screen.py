from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be
from selene.support.shared.jquery_style import s


class MediaScreen:
    """Класс для работы с экраном медиа"""

    def __init__(self):
        """Инициализация элементов экрана"""
        self.media_screen_title = (AppiumBy.ID, "ru.kinopoisk:id/title_logo")
        self.all_cinema_button = (
            AppiumBy.ACCESSIBILITY_ID,
            "ru.kinopoisk:id/cinema_title_text_view",
        )
        self.premiere_title = (AppiumBy.LINK_TEXT, "График премьер")
        self.refresh_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Обновить']",
        )

    @step("Проверяем наличие кнопки 'Обновить'")
    def refresh_button_is_present(self) -> "MediaScreen":
        s(self.refresh_button).should(EC.by_and(be.clickable))
        return self
