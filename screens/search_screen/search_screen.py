from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.condition import Condition as EC
from selene import be, have
from selene.support.shared.jquery_style import s, ss


class SearchScreen:
    """Класс для работы с экраном поиска"""
    def __init__(self):
        """Инициализация элементов экрана"""
        self.search_input = (AppiumBy.ID, 'ru.kinopoisk:id/search_edit_text')
        self.movies_catalog = (AppiumBy.ID, 'ru.kinopoisk:id/movies_catalog')
        self.category_by_name = (
            AppiumBy.ID,  # TODO! to fixed this locator
            "//android.widget.TextView[@resource-id=ru.'kinopoisk:id/title_text_view 'and @text='{category_name}}']"
        )
        self.back_button = (
            AppiumBy.ID,
            "ru.kinopoisk:id/back_button_container",
        )
        self.list_of_all_search_results = (
            AppiumBy.ID,
            "ru.kinopoisk:id/title",
        )
        self.list_of_all_categories = (
            AppiumBy.ID,
            "ru.kinopoisk:id/title_text_view",
        )

    @step("Проверяем открытие экрана поиска")
    def check_search_screen_is_opened(self) -> "SearchScreen":
        s(self.search_input).should(EC.by_and(be.visible))
        return self

    @step("Нажимаем на поле ввода для поиска фильмов и вводим значение {to_search}")
    def click_search_input_and_type_of_value(self, to_search: str) -> "SearchScreen":
        s(self.search_input).should(EC.by_and(be.visible)).click().type(to_search)
        return self

    @step("Проверяем отображение поисковый выдачи и наличие ожидаемого результата {expected_result}")
    def check_search_results(self, expected_result: str) -> "SearchScreen":
        results = ss(self.list_of_all_search_results)
        results.should(EC.by_and(have.size_greater_than(0))).first.should(
            have.text(expected_result))
        return self

    @step("Проверяем отображение категории по наименованию {category_name}")
    def check_category_is_present(self, category_name: str) -> "SearchScreen":
        categories = ss(self.list_of_all_categories)
        categories.should(EC.by_and(have.size_greater_than(0)))
        categories.element_by(have.text(category_name)).should(EC.by_and(be.visible))
        return self

    @step("Нажимаем на категорию по ее наименованию {category_name}")
    def tap_category_by_name(self, category_name: str) -> "SearchScreen":
        ss(self.list_of_all_categories).element_by(
            have.text(category_name)).should(EC.by_and(be.clickable)).click()
        return self
