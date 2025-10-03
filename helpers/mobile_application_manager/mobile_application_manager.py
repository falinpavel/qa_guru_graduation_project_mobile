from screens.welcome_screen.welcome_screen import WelcomeScreen


class MobileApplicationManager:
    def __init__(self):
        self.welcome_screen = WelcomeScreen()


kinopoisk_app = MobileApplicationManager()
