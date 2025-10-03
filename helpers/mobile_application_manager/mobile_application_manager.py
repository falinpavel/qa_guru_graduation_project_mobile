from screens.welcome_screen.welcome_screen import WelcomeScreen
from utils.mobile_actions.swiper_helper import SwipeShortcuts


class MobileApplicationManager:
    def __init__(self):
        self.welcome_screen = WelcomeScreen()
        # Хелпер для свайпов по экрану
        self.mobile_actions = SwipeShortcuts()


kinopoisk_app = MobileApplicationManager()
