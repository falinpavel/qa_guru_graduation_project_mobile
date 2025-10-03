from screens.welcome_screen.welcome_screen import WelcomeScreen
from utils.mobile_actions.swiper_helper import SwipeShortcuts


class MobileApplicationManager:
    """Класс для управления мобильным приложением.
    Является единой точкой входа во все приложения и на все его экраны и элементы"""

    def __init__(self):
        """Инициализация экранов и хелперов"""
        self.welcome_screen = WelcomeScreen()
        # Хелпер для свайпов по экрану
        self.mobile_actions = SwipeShortcuts()


kinopoisk_app = MobileApplicationManager()
