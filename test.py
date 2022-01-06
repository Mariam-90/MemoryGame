import unittest
import database


class test(unittest.TestCase):

    def test_login(self):
        lucas = User(username="lucas", email="lucas@example.com", password="test")
        db.session.add(lucas)

        rv = self.login('lucas', 'test')
        assert 'Welcome' in rv.data