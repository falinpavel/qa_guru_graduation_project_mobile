import base64

import allure
import pytest
import allure_commons
import os

from allure_commons._allure import step
from appium import webdriver as appium_webdriver
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
    # Путь для сохранения видео
    video_dir = os.path.join(os.getcwd(), "resources", "appium_video_records")
    os.makedirs(video_dir, exist_ok=True)

    is_local_recording = context in ["emulator_device", "connected_device"]
    if is_local_recording:
        browser.driver.start_recording_screen(videoFps='30')

    yield

    if is_local_recording:
        video_raw = browser.driver.stop_recording_screen()
        # Можно сделать имя файла по имени теста, если нужно
        video_name = f"{context}_test_video.mp4"
        video_path = os.path.join(video_dir, video_name)
        with open(video_path, "wb") as video_file:
            video_file.write(base64.b64decode(video_raw))

        allure.attach.file(
            video_path,
            name="Test video",
            attachment_type=allure.attachment_type.MP4
        )

    allure_attachments.attach_screenshot()
    allure_attachments.attach_xml_dump()

    session_id = browser.driver.session_id

    with step("Закрываем сессию мобильного приложения"):
        browser.quit()

    allure_attachments.attach_bstack_video(
        session_id
    ) if context == "bstack_device" else None


@pytest.fixture()
def disable_network():
    """Фикстура для временного отключения интернета на девайсе.
    По окончании теста интернет включается обратно"""
    driver = browser.driver
    try:
        with step(f"Отключаем интернет"):
            # Полное отключение интернета
            driver.set_network_connection(0)  # DISCONNECTION
    except Exception as e:
        raise e

    yield

    try:
        with step(f"Включаем интернет"):
            # Полное включение интернета
            driver.set_network_connection(6)  # CONNECTION
    except Exception as e:
        raise e
