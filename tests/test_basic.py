#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app
import unittest


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.uri = 'http://127.0.0.1:5000'
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()


