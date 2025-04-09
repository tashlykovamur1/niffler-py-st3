import pytest

from tests.niffler import Niffler


@pytest.mark.ui
@pytest.mark.ui_friends
class TestFriends(Niffler):

    def test_empty_friends_page_by_default(self, login_user):
        """ По дефолту открывается страница без друзей для нового юзера"""
        self.friends_page.open()
        self.friends_page.check_no_friends_on_page()
