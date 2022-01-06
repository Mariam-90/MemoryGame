import unittest
import database
from database import db

class databaseTest(unittest.TestCase):
    def test_about_page(self):
        response = self.client.get('/database')
        self.assertRedirects(response, '/database/', status_code=301, target_status_code=200, msg_prefix='',
                             fetch_redirect_response=True)




    def test_login(self):
        lucas = self(email="lucas@example.com", password="test")
        db.session.add(lucas)

        rv = self.login('lucas', 'test')
        assert 'Welcome' in rv.data





    def test_login2(self):
        response = self.client.get(('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/database.html")

    def test_signup(self):
        lucas = self(username="lucas", email="lucas@example.com", password="test")
        user2 = self(username="lucas", email="lucas@test.com")


        assert lucas in db.session
        assert user2 not in db.session

    def test_login(self):
        lucas = self(username="lucas", email="lucas@example.com", password="test")
        db.session.add(lucas)


        rv = self.login('lucas', 'test')
        assert 'Welcome' in rv.data

    def test_insert_board(self):
        database.Database()
        database.insert_board('a')
        database.delete_board('a')
        self.assertFalse(database.checkboard('a'))

    def test_login2(self):

        database.insert_user('m', 'm', 'm', 'm', 'm', 'm', 'Famle', 'm', 'm', 'm', 'm', 'm')
        self.assertEqual('mm', database.login2('m'))

    def test_login3(self):
        database.insert_user('m', 'm', 'm', 'm', 'm', 'm', 'Famle', 'm', 'm', 'm', 'm', 'm')
        database.login3('m', 222)
        self.assertNotEqual('m', database.login3('m'))

if __name__ == '__main__':
    unittest.main()
