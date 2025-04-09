from typing import Union

from hamcrest import assert_that, equal_to, is_not
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EXPLICIT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=EXPLICIT_TIMEOUT)

    def element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def open(self, url: str = None):
        self.driver.get(f"{self.base_url}{url}" if url else self.base_url)

    def url_should_be(self, expected_url: str):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f"Expected url to be {expected_url}, but was {self.driver.current_url}",
        )

    def click(self, locator: tuple[str, str]):
        self.should_be_clickable(locator)
        self.element(locator).click()

    def send_keys(self, locator: tuple[str, str], text: str = ""):
        self.element(locator).send_keys(text)

    def should_be_clickable(self, locator: Union[WebElement, tuple[str, str]]):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} still not clickable",
        )

    def should_be_not_clickable(self, locator: tuple[str, str]):
        assert_that(
            self.element(locator).is_enabled(),
            equal_to(False),
            f"Element {locator} is clickable",
        )

    def should_be_visible(
            self,
            locator: tuple[str, str],
    ):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} still not visible",
        )

    def should_be_invisible(
            self,
            locator: tuple[str, str],
    ):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Element {locator} still visible",
        )

    def should_contain_text(self, locator: tuple[str, str], text: str):
        self.should_be_visible(locator)
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Element {locator} still not contains text {text}, actual text: {self.element(locator).text}",
        )

    def should_contain_text_in_value(self, locator: tuple[str, str], text: str):
        self.should_be_visible(locator)
        self.wait.until(
            EC.text_to_be_present_in_element_value(locator, text),
            message=f"Element {locator} still not contains text {text} in value, "
                    f"actual text: {self.element(locator).get_attribute('value')}",
        )

    def should_have_text_in_attribute(
            self, locator: tuple[str, str], attribute: str, text: str
    ):
        self.should_be_visible(locator)
        self.wait.until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, text),
            message=f"Element {locator} still not contains text {text} in attribute {attribute}, "
                    f"actual text: {self.element(locator).get_attribute(attribute)}",
        )

    def should_have_attribute(self, locator: tuple[str, str], attribute: str):
        assert_that(self.element(locator).get_attribute(attribute), is_not(None))

    def execute_script(self, js_script: str, args: str = None):
        return self.driver.execute_script(js_script, args)
