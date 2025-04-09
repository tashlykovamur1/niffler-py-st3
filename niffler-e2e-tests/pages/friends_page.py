from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FriendsPage(BasePage):
    FRIENDS_TAB = (By.XPATH, '//h2[text()="Friends"]')
    NO_FRIENDS_TITLE = (By.XPATH, '//*[text()="There are no users yet"]')
    IMG = (By.CSS_SELECTOR, 'img[alt="Lonely niffler"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[aria-label="search"]')
    SEARCH_BTN = (By.ID, 'input-submit')

    def check_search_field_is_visible(self):
        self.should_be_visible(self.SEARCH_FIELD)
        self.should_be_clickable(self.SEARCH_BTN)

    def check_friends_page_is_opened(self):
        self.url_should_be(FRIENDS_URL)
        self.check_search_field_is_visible()
        self.should_be_visible(self.FRIENDS_TAB)

    def check_no_friends_on_page(self):
        self.should_be_visible(self.NO_FRIENDS_TITLE)
        self.should_have_text_in_attribute(self.IMG, attribute="src", text="/assets/niffler-with-a-coin-Cb77k8MX.png")
