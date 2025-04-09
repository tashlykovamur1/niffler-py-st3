from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls_data import MAIN_URL


class MainPage(BasePage):
    _SPENDINGS_HISTORY_TITLE = (By.XPATH, '//h2[text()="History of Spendings"]')

    def check_main_page_is_opened(self):
        self.url_should_be(MAIN_URL)
        self.should_be_visible(self._SPENDINGS_HISTORY_TITLE)
