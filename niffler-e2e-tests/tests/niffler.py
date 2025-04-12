from selenium.webdriver.chrome.webdriver import WebDriver

from pages.friends_page import FriendsPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from urls_data import LOGIN_URL, REGISTER_URL, FRIENDS_URL, MAIN_URL


class Niffler:
    driver: WebDriver
    login_page: LoginPage
    register_page: RegisterPage
    main_page: MainPage
    friends_page: FriendsPage
    header: Header

    def setup_method(self):
        self.login_page = LoginPage(self.driver, base_url=LOGIN_URL)
        self.register_page = RegisterPage(self.driver, base_url=REGISTER_URL)
        self.main_page = MainPage(self.driver, base_url=MAIN_URL)
        self.friends_page = FriendsPage(self.driver, base_url=FRIENDS_URL)
        self.header = Header(self.driver, base_url=MAIN_URL)
