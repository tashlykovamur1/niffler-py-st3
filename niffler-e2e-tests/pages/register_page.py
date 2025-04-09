from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    _FORM_HEADER = (By.CSS_SELECTOR, 'h1[class="header"]')
    _USERNAME_INPUT = (By.NAME, "username")
    _PASSWORD_INPUT = (By.NAME, "password")
    _PASSWORD_SUBMIT = (By.NAME, "passwordSubmit")
    _REGISTER_SUCCEED_MSG = (By.CSS_SELECTOR, '[class*="form__paragraph_success"]')
    _SIGN_UP_BTN = (By.XPATH, '//button[@class="form__submit"][normalize-space()="Sign Up"]')
    _REGISTER_SIGN_IN_BTN = (By.CSS_SELECTOR, '[class="form_sign-in"]')
    _ERROR_MSG = (By.CLASS_NAME, 'form__error')
    _USERNAME_ERROR_MSG = (By.XPATH, '//label[contains(text(), "Username")]/*[@class="form__error"]')
    _PASSWORD_ERROR_MSG = (By.XPATH, '//label[contains(text(), "Password")]/*[@class="form__error"]')
    _SUBMIT_PASSWORD_ERROR_MSG = (By.XPATH, '//label[contains(text(), "Submit password")]/*[@class="form__error"]')
    _LOGIN_HREF = (By.XPATH, f'//a[@href="{MAIN_URL}"][text()="Log in!"]')

    def input_password(self, password: str):
        self.should_have_attribute(self._PASSWORD_INPUT, attribute="required")
        self.should_have_text_in_attribute(self._PASSWORD_INPUT, attribute="type", text="password")
        self.send_keys(self._PASSWORD_INPUT, text=password)

    def input_username(self, name: str):
        self.should_have_attribute(self._USERNAME_INPUT, attribute="required")
        self.send_keys(self._USERNAME_INPUT, text=name)

    def input_submit_password(self, password: str):
        self.should_have_attribute(self._PASSWORD_SUBMIT, attribute="required")
        self.should_have_text_in_attribute(self._PASSWORD_SUBMIT, attribute="type", text="password")
        self.send_keys(self._PASSWORD_SUBMIT, text=password)

    def register(self, user_data: dict[str, str]):
        self.url_should_be(expected_url=REGISTER_URL)
        self.should_contain_text(self._FORM_HEADER, text="Sign up")

        self.input_username(user_data["username"])
        self.input_password(user_data["password"])
        self.input_submit_password(user_data.get("submit_password", user_data["password"]))

        self.click(self._SIGN_UP_BTN)

    def check_register_succeed(self):
        self.should_contain_text(self._REGISTER_SUCCEED_MSG, text="Congratulations! You've registered!")
        self.should_be_clickable(self._REGISTER_SIGN_IN_BTN)

    def check_length_validation(self):
        self.should_contain_text(self._USERNAME_ERROR_MSG,
                                 text="Allowed username length should be from 3 to 50 characters")
        self.should_contain_text(self._PASSWORD_ERROR_MSG,
                                 text="Allowed password length should be from 3 to 12 characters")
        self.should_contain_text(self._SUBMIT_PASSWORD_ERROR_MSG,
                                 text="Allowed password length should be from 3 to 12 characters")

    def check_equal_passwords_validation(self):
        self.should_contain_text(self._PASSWORD_ERROR_MSG, text="Passwords should be equal")

    def go_to_login_page(self):
        self.click(self._LOGIN_HREF)
