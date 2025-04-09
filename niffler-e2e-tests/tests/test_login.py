import pytest

from conftest import faker
from tests.niffler import Niffler


@pytest.mark.ui
@pytest.mark.ui_login
@pytest.mark.usefixtures("open_login_page")
class TestLogin(Niffler):

    def test_login_by_existed_user(self, register_user):
        """ Авторизация под существующим юзером """
        user_data = {"username": register_user["username"], "password": register_user["password"]}

        self.login_page.login(user_data)
        self.main_page.check_main_page_is_opened()

    def test_create_new_account_from_login_page(self):
        """ Регистрация нового юзера со страницы авторизации """
        user_data = {"username": faker.name(), "password": faker.password(length=6)}

        self.login_page.go_to_register_page()
        self.register_page.register(user_data)
        self.register_page.check_register_succeed()

    def test_reveal_password_by_eye_btn(self):
        """ Отображение пароля в поле по клику на глазик """

        self.login_page.input_password(password=faker.password(length=5))
        self.login_page.show_password()
        self.login_page.check_password_is_revealed()

    def test_login_with_invalid_creds(self):
        """ Авторизация под несуществующим юзером """
        unexisted_user = {"username": faker.name(), "password": faker.password(length=5)}

        self.login_page.login(user_data=unexisted_user)
        self.login_page.check_error_msg_is_visible()
