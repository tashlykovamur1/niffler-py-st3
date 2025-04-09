from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls_data import LOGIN_URL


class LoginPage(BasePage):
    _FORM_HEADER = (By.CSS_SELECTOR, 'h1[class="header"]')
    _LOGIN_FORM = (By.CSS_SELECTOR, '[class="form"][action="/login"]')
    _USERNAME_INPUT = (By.NAME, "username")
    _PASSWORD_INPUT = (By.NAME, "password")
    _SHOW_PSWD_BTN = (By.CSS_SELECTOR, '[class*="form__password-button"]')
    _LOG_IN_BTN = (By.XPATH, '//button[@class="form__submit"][normalize-space()="Log in"]')
    _ERROR_MSG = (By.CLASS_NAME, 'form__error')
    _REGISTER_BTN = (By.CSS_SELECTOR, '[class="form__register"]')

    def input_password(self, password: str):
        self.should_have_attribute(self._PASSWORD_INPUT, attribute="required")
        self.should_have_text_in_attribute(self._PASSWORD_INPUT, attribute="type", text="password")
        self.send_keys(self._PASSWORD_INPUT, text=password)

    def input_username(self, name: str):
        self.should_have_attribute(self._USERNAME_INPUT, attribute="required")
        self.send_keys(self._USERNAME_INPUT, text=name)

    def show_password(self):
        self.click(self._SHOW_PSWD_BTN)

    def check_password_is_revealed(self):
        self.should_have_text_in_attribute(self._PASSWORD_INPUT, attribute="type", text="text")

    def login(self, user_data: dict[str, str]):
        self.input_username(user_data["username"])
        self.input_password(user_data["password"])

        self.click(self._LOG_IN_BTN)

    def check_login_page_is_opened(self):
        self.url_should_be(LOGIN_URL)
        self.should_contain_text(self._FORM_HEADER, text="Log in")
        self.should_be_visible(self._LOGIN_FORM)

    def check_error_msg_is_visible(self):
        self.should_contain_text(self._ERROR_MSG, text="Неверные учетные данные пользователя")

    def go_to_register_page(self):
        self.click(self._REGISTER_BTN)
