import pytest

from conftest import faker
from tests.niffler import Niffler


@pytest.mark.ui
@pytest.mark.ui_register
@pytest.mark.usefixtures("open_register_page")
class TestRegister(Niffler):

    @pytest.mark.parametrize(
        "name_length, password_length", (
                [1, 1],
                [2, 2],
                [51, 13],
        )
    )
    def test_length_validation_in_signup_form(self, name_length, password_length):
        """ Регистрация с невалидной длиной полей """
        username = faker.random_letters(length=name_length)
        password = faker.random_letters(length=password_length)

        self.register_page.register(user_data={"username": username, "password": password})
        self.register_page.check_length_validation()

    def test_redirect_on_login_page(self):
        """ Редирект с формы регистрации на форму логина """
        self.register_page.go_to_login_page()
        self.login_page.check_login_page_is_opened()

    def test_signup_with_mismatched_passwords(self):
        """ Пароль и подтверждающий пароль не совпадают """
        user_data = {
            "username": faker.name(),
            "password": faker.password(length=6),
            "submit_password": faker.password(length=5)
        }

        self.register_page.register(user_data)
        self.register_page.check_equal_passwords_validation()
