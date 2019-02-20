from .base_test import *
from flask import current_app


class TestDevelopmentConfig(BaseTestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app.config.from_object('instance.config.DevelopmentConfig')

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertTrue(self.app.config['TESTING'] is False)
        self.assertTrue(self.app.config['DATABASE_URL'] ==
                        'postgres://admin:admin123@localhost:5432/politico')


class TestTestingConfig(BaseTestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config.from_object('instance.config.TestingConfig')

    def test_app_is_testing(self):
        self.assertFalse(current_app is None)
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertTrue(self.app.config['TESTING'] is True)
        self.assertTrue(self.app.config['DATABASE_URL'] ==
                        'postgres://admin:admin123@localhost:5432/politico_test')


if __name__ == "__main__":
    unittest.main()
