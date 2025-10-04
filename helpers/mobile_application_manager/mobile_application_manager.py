from components.navigation_bar.navigation_bar import NavigationBar
from components.top_navigation_home_screen.top_navigation_home_screen import TopNavigationHomeScreen
from screens.home_screen.home_screen import HomeScreen
from screens.welcome_screen.welcome_screen import WelcomeScreen
from utils.mobile_actions.swiper_helper import SwipeShortcuts


class MobileApplicationManager:
    """Класс для управления мобильным приложением.
    Является единой точкой входа во все приложения и на все его экраны и элементы.
    Использует паттерн Fluent Page Object."""

    def __init__(self):
        """Инициализация экранов и хелперов"""
        # Экраны приложения
        self.welcome_screen = WelcomeScreen()
        self.home_screen = HomeScreen()
        # Общие навигационные компоненты приложения
        self.navigation_bar = NavigationBar()
        self.top_navigation_home_screen = TopNavigationHomeScreen()
        # Хелпер для свайпов по экрану
        self.mobile_actions = SwipeShortcuts()


kinopoisk_app = MobileApplicationManager()
