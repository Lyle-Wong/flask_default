# -*- coding=utf-8 -*-

import unittest
from application import create_app
from flask import current_app

class TestAppExists(unittest.TestCase):

    def setUp(self):
        self.app = create_app('develop')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exist(self):
        self.assertTrue(current_app)


if __name__ == '__main__':
    unittest.main()