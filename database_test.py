import unittest
import database

email = []
password = []


class databaseTest(unittest.TestCase):

    def test_database_login(self):
        r = database.login(email='maryam80@gmail.com', password='123456d')
        print("login", r)
        self.assertTrue(r)

    def test_database_login2(self):
        r = database.login(email='tomadal@gmail.com', password='123456t')
        print(" login2", r)
        self.assertTrue(r)

    def test_database_login3(self):
        r = database.login(email='maryam7@gmail.com', password='123456a')
        print(" login3", r)
        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()
