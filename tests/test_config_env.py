#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_basic import BasicTestCase
from flask import current_app


class TestConfigEnv(BasicTestCase):

    def test_app_exits(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(not current_app.config['TESTING'])


