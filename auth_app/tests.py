from django.test import TestCase
from auth_app.services import create_user, activate_user, user_by_id


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self._user = create_user("user1@mail.ru", "user1")

    def test_creating_new_user(self) -> None:
        user = create_user("user2@mail.ru", "user2")
        self.assertNotEqual(user, None)

    def test_activate_user(self) -> None:
        self._user.is_active = False
        activate_user(self._user)
        self.assertEqual(self._user.is_active, True)

    def test_user_by_id(self) -> None:
        user = user_by_id(self._user.id)
        self.assertEqual(self._user.id, user.id)
