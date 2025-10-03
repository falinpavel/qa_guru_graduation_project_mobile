from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selene import browser
import time


class MobileGestures:
    """
    Современные мобильные жесты для Appium 2.0+
    """

    @staticmethod
    def swipe(direction, duration=1000):
        """
        Свайп через W3C Actions

        Args:
            direction: 'up', 'down', 'left', 'right'
            duration: длительность в миллисекундах
        """
        # Получаем размеры экрана
        window_size = browser.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']

        # Координаты для свайпов
        swipe_coords = {
            'up': (width * 0.5, height * 0.8, width * 0.5, height * 0.2),
            'down': (width * 0.5, height * 0.2, width * 0.5, height * 0.8),
            'left': (width * 0.8, height * 0.5, width * 0.2, height * 0.5),
            'right': (width * 0.2, height * 0.5, width * 0.8, height * 0.5)
        }

        if direction not in swipe_coords:
            raise ValueError(f"Direction must be 'up', 'down', 'left' or 'right', got '{direction}'")

        start_x, start_y, end_x, end_y = swipe_coords[direction]

        # ПРАВИЛЬНОЕ использование ActionBuilder
        actions = ActionChains(browser.driver)

        # СОЗДАЕМ и ДОБАВЛЯЕМ pointer input с правильными параметрами
        finger = PointerInput(POINTER_TOUCH, name="finger")
        actions.w3c_actions.add_pointer_input(kind="touch", name=finger)  # ← ПРАВИЛЬНО!

        # Выполняем свайп
        (actions.w3c_actions.pointer_action
         .move_to_location(start_x, start_y)
         .pointer_down()
         .move_to_location(end_x, end_y)
         .pause(duration / 1000)
         .pointer_up())

        actions.w3c_actions.perform()
        time.sleep(0.5)



class SwipeShortcuts:
    """Упрощенные методы для частых операций"""

    @staticmethod
    def swipe_right(duration=500):
        """Свайп вправо"""
        MobileGestures.swipe(direction='right', duration=duration)

    @staticmethod
    def swipe_left(duration=500):
        """Свайп влево"""
        MobileGestures.swipe(direction='left', duration=duration)

    @staticmethod
    def swipe_up(duration=500):
        """Свайп вверх"""
        MobileGestures.swipe(direction='up', duration=duration)

    @staticmethod
    def swipe_down(duration=500):
        """Свайп вниз"""
        MobileGestures.swipe(direction='down', duration=duration)

    @staticmethod
    def swipe_multiple(direction, count=3, duration=500):
        """Несколько свайпов подряд"""
        for _ in range(count):
            MobileGestures.swipe(direction=direction, duration=duration)
            time.sleep(0.2)
