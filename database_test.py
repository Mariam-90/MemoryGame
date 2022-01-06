import unittest
import database

email = []
password = []
confirmpass = []


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

    def test_database_signup(self):
        c = '123456ff'
        d = '123456ff'
        a = database.signup(email='maryam09rr@gmail.com', password=c,confirmpass=d)
        self.assertEqual(a, d == c)

    def test_database_signup2(self):
        c = '123456ff'
        d = '123456ff'
        a = database.signup2(email='maryam09mm@gmail.com', password=c, confirmpass=d)
        self.assertEqual(a, d == c)

    def test_database_signup3(self):
        c = '123456ff'
        d = '123456ff'
        a = database.signup3(email='maryammmm@gmail.com', password=c, confirmpass=d)
        self.assertEqual(a, d == c)


if __name__ == '__main__':
    unittest.main()
