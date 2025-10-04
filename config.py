import os

from pathlib import Path
from appium.options.android import UiAutomator2Options


def get_apk_path() -> str:
    """Получает абсолютный путь к APK из относительного пути
    хранящегося в .env файле"""
    relative_path = os.getenv("APK_FILE_PATH")
    if not relative_path:
        raise ValueError("APK_FILE_PATH не указан в .env файле")

    project_root = Path(__file__).parent
    apk_path = project_root / relative_path

    if not apk_path.exists():
        raise FileNotFoundError(f"APK файл не найден: {apk_path}")
    return str(apk_path)


def options_management(context) -> UiAutomator2Options:
    """Проверяем полученный на вход context и в зависимости
    от него настраиваем и возвращаем соответствующие options"""
    options = UiAutomator2Options()

    if context in ["emulator_device", "connected_device"]:
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = os.getenv("DEVICE_NAME")
        options.app = get_apk_path()
        options.set_capability(
            name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH")
        )

    if context == "bstack_device":
        options.platform_name = "Android"
        options.device_name = os.getenv("DEVICE_NAME")
        options.platform_version = os.getenv("PLATFORM_VERSION")
        options.app = os.getenv("APK_FILE_PATH")
        options.set_capability(
            name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH")
        )
        options.set_capability(
            name="bstack:options",
            value={
                "projectName": "Дипломный проект по автоматизации мобильных приложений",
                "buildName": "browserstack-graduation-project-build-1",
                "sessionName": "context_bs_device_session",
                "userName": os.getenv("BS_LOGIN"),
                "accessKey": os.getenv("BS_PASSWORD"),
                "networkLogs": True,
                "deviceLogs": True,
                "debug": True,
                "idleTimeout": 300,
                "acceptInsecureCerts": True,
            },
        )
        options.set_capability(
            name="appium.options",
            value={"autoGrantPermissions": True, "noReset": False, "fullReset": True},
        )

    return options
