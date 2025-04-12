import pytest

from tests.niffler import Niffler


@pytest.mark.ui
@pytest.mark.ui_header
class TestHeader(Niffler):

    def test_logout_from_header(self, login_user):
        """ Логаут из системы """
        self.header.logout(action="logout")
        self.login_page.check_login_page_is_opened()

    def test_close_logout_modal(self, login_user):
        """ Закрытие модалки логаута (отмена логаута) """
        self.header.logout(action="close")
        self.header.check_logout_modal_is_invisible()
