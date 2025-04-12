from typing import Literal

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):
    _NEW_SPENDING_BTN = (By.XPATH, '//a[text()="New spending"][@href="/spending"]')
    _NIFFLER_LOGO = (By.XPATH, '//h1[text()="Niffler"]//ancestor::*[@href="/main"]')
    _AVATAR_BTN = (By.CSS_SELECTOR, 'button[aria-label="Menu"]')
    _MENU = (By.CSS_SELECTOR, 'ul[role="menu"]')
    _MENU_ITEM_PROFILE = (By.XPATH, '//a[text()="Profile"][@href="/profile"]')
    _MENU_ITEM_FRIENDS = (By.XPATH, '//a[text()="Friends"][@href="/people/friends"]')
    _MENU_ITEM_ALL_PEOPLE = (By.XPATH, '//a[text()="All People"][@href="/people/all"]')
    _MENU_ITEM_SIGN_OUT = (By.XPATH, '//li[text()="Sign out"]')
    _SIGN_OUT_MODAL = (By.XPATH, '//h2[text()="Want to logout?"]/parent::*[@role="dialog"]')
    _SIGN_OUT_MODAL_TITLE = (By.XPATH, '//h2[text()="Want to logout?"]')
    _SIGN_OUT_MODAL_SUBTITLE = (By.ID, 'alert-dialog-slide-description')
    _SIGN_OUT_MODAL_LOGOUT_BTN = (By.XPATH, '//button[text()="Log out"]')
    _SIGN_OUT_MODAL_CLOSE_BTN = (By.XPATH, '//button[text()="Close"]')

    def open_menu(self):
        self.click(self._AVATAR_BTN)
        self.should_be_visible(self._MENU)
        for item in (
                self._MENU_ITEM_PROFILE,
                self._MENU_ITEM_FRIENDS,
                self._MENU_ITEM_ALL_PEOPLE,
                self._MENU_ITEM_SIGN_OUT,
        ):
            self.should_be_clickable(item)

    def logout(self, action: Literal["logout", "close"]):
        self.open_menu()
        self.click(self._MENU_ITEM_SIGN_OUT)
        self.check_logout_modal_is_visible()
        self.click(self._SIGN_OUT_MODAL_LOGOUT_BTN if action == "logout" else self._SIGN_OUT_MODAL_CLOSE_BTN)

    def check_logout_modal_is_visible(self):
        self.should_be_visible(self._SIGN_OUT_MODAL)
        self.should_be_visible(self._SIGN_OUT_MODAL_TITLE)
        self.should_contain_text(self._SIGN_OUT_MODAL_SUBTITLE, text="If you are sure, submit your action.")
        self.should_be_clickable(self._SIGN_OUT_MODAL_LOGOUT_BTN)
        self.should_be_clickable(self._SIGN_OUT_MODAL_CLOSE_BTN)

    def check_logout_modal_is_invisible(self):
        self.should_be_invisible(self._SIGN_OUT_MODAL)
