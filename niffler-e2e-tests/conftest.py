import pytest
import requests
from faker import Faker
from hamcrest import equal_to, assert_that
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.niffler import Niffler
from urls_data import REGISTER_URL

faker = Faker()


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--enable-automation")
    options.add_argument("--enable-javascript")
    options.add_argument(
        "--no-sandbox"
    )
    options.add_argument(
        "--disable-dev-shm-usage"
    )
    options.add_argument(
        "--disable-search-engine-choice-screen"
    )  # со 127 версии хрома для отключения поискового движка

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    request.cls.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def register_user():
    """ Регистрация юзера по апи """

    with requests.Session() as session:
        get_response = session.get(REGISTER_URL)
        password = faker.password(length=5)
        user_data = {
            'username': faker.name(),
            'password': password,
            'passwordSubmit': password,
            '_csrf': get_response.cookies['XSRF-TOKEN']
        }
        response = session.post(REGISTER_URL, data=user_data)

    assert_that(response.status_code, equal_to(201), "Не удалось зарегистрировать пользователя")
    user_data.pop('passwordSubmit')
    yield user_data


@pytest.fixture(scope="function")
def pages(driver):
    niffler = Niffler()
    niffler.driver = driver
    niffler.setup_method()
    yield niffler


@pytest.fixture(scope="function")
def login_user(register_user, pages):
    """ Авторизация зарегистрированного юзера через ui """
    pages.login_page.open()
    pages.login_page.check_login_page_is_opened()

    register_user.pop('_csrf')
    pages.login_page.login(user_data=register_user)
    pages.main_page.check_main_page_is_opened()


@pytest.fixture(scope="function")
def open_register_page(pages):
    pages.register_page.open()


@pytest.fixture(scope="function")
def open_login_page(pages):
    pages.login_page.open()
    pages.login_page.check_login_page_is_opened()
