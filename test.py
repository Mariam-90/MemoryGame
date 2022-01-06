import unittest
import database


class test(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.client = None

    def test_login(self):
        lucas = User(username="lucas", email="lucas@example.com", password="test")
        db.session.add(lucas)

        rv = self.login('lucas', 'test')
        assert 'Welcome' in rv.data