from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be, have
from selene.support.shared.jquery_style import s


class SearchScreen:
    """Класс для работы с экраном поиска"""
    def __init__(self):
        """Инициализация элементов экрана"""
        self.search_input = (AppiumBy.ID, 'ru.kinopoisk:id/search_edit_text')
        self.movies_catalog = (AppiumBy.ID, 'ru.kinopoisk:id/movies_catalog')
        self.category_by_name = (
            AppiumBy.ID,
            "//android.widget.TextView[@resource-id=ru.'kinopoisk:id/title_text_view 'and @text='{category_name}}']"
        )
        self.back_button = (
            AppiumBy.ID,
            "ru.kinopoisk:id/back_button_container",
        )
        self.title_of_first_result = (
            AppiumBy.ID,
            "ru.kinopoisk:id/title",
        )

    @step("Проверка открытия экрана поиска")
    def check_search_screen_is_opened(self) -> "SearchScreen":
        s(self.search_input).should(EC.by_and(be.visible))
        return self

    @step("Нажать на поле ввода для поиска фильмов")
    def click_search_input_and_type_of_value(self, to_search: str) -> "SearchScreen":
        s(self.search_input).should(EC.by_and(be.visible)).click().type(to_search)
        return self

    @step("Проверка отображения первого результата")
    def check_first_search_result(self, expected_result: str) -> "SearchScreen":
        s(self.title_of_first_result).should(EC.by_and(be.visible, have.text(expected_result)))
        return self
