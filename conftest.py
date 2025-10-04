import time

import pytest
import allure_commons
import os

from allure_commons._allure import step
from appium import webdriver as appium_webdriver
from appium.webdriver.extensions.android.network import Network
from dotenv import load_dotenv
from selene import browser, support

from config import options_management
from utils.allure import allure_attachments


def pytest_addoption(parser: pytest.Parser) -> None:
    """Добавляем опцию запуска --context для выбора устройства"""
    parser.addoption(
        "--context",
        default="emulator_device",
        choices=["bstack_device", "connected_device", "emulator_device"],
        help="Выберите девайс на котором будут запущены тесты",
    )


def pytest_configure(config: pytest.Config) -> None:
    """Конфигурируем окружение и в зависимости от context выбираем файл .env"""
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    """Получаем значение опции --context"""
    return request.config.getoption("--context")


@pytest.fixture(scope="function", autouse=True)
def mobile_management(context):
    """Принимаем сконфигурированне опции и запускаем мобильное приложение,
    а также добавляем хендлеры для сбора скриншотов и xml дампа по окончании теста"""
    appium_options = options_management(context=context)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with step("Инициализируем сессию мобильного приложения"):
        browser.config.driver = appium_webdriver.Remote(
            command_executor=appium_options.get_capability(name="EXECUTABLE_PATH"),
            options=appium_options,
        )

    browser.config.timeout = float(os.getenv("TIMEOUT", "10.0"))

    yield

    allure_attachments.attach_screenshot()
    allure_attachments.attach_xml_dump()

    session_id = browser.driver.session_id

    with step("Закрываем сессию мобильного приложения"):
        browser.quit()

    allure_attachments.attach_bstack_video(
        session_id
    ) if context == "bstack_device" else None


@pytest.fixture()
def disable_internet():
    """Фикстура для временного отключения интернета на девайсе.
    Для использования необходимо передать в тестовую функцию и внутри теста вызвать
    данную фикстуру: disable_internet()"""
    def _disable_internet():
        # Используем существующий драйвер из browser
        driver = browser.driver
        try:
            with step(f"Отключаем интернет"):
                # Полное отключение интернета
                driver.set_network_connection(0)  # NO_CONNECTION
        except Exception as e:
            raise e
    return _disable_internet


@pytest.fixture()
def enable_network():
    """Фикстура для включения интернета на устройстве"""
    def _enable_internet():
        # Используем существующий драйвер из browser
        driver = browser.driver
        try:
            with step(f"Включаем интернет"):
                # Полное отключение интернета
                driver.set_network_connection(6)  # NO_CONNECTION
        except Exception as e:
            raise e
    return _enable_internet
