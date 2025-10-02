import os

from pathlib import Path
from appium.options.android import UiAutomator2Options


def get_apk_path():
    """Получает абсолютный путь к APK из относительного пути в .env"""
    relative_path = os.getenv("APK_FILE_PATH")
    if not relative_path:
        raise ValueError("APK_FILE_PATH не указан в .env файле")

    project_root = Path(__file__).parent
    apk_path = project_root / relative_path

    if not apk_path.exists():
        raise FileNotFoundError(f"APK файл не найден: {apk_path}") # Для отладки
    return str(apk_path)


def options_management(context):
    options = UiAutomator2Options()

    apk_absolute_path = get_apk_path()

    if context in ['emulator_device', 'connected_device']:
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = os.getenv("DEVICE_NAME")
        options.app = apk_absolute_path
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))

    if context == 'bstack_device':
        options.platform_name = "Android"
        options.device_name = os.getenv("DEVICE_NAME")
        options.app = os.getenv("APK_FILE_PATH")
        options.set_capability(name="EXECUTABLE_PATH", value=os.getenv("EXECUTABLE_PATH"))
        options.set_capability(name="bstack:options", value={
            "projectName": "Mobile graduation project qa_guru",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack session",
            "userName": os.getenv("BS_LOGIN"),
            "accessKey": os.getenv("BS_PASSWORD")
        })

    return options