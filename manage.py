#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app
from flask_script import Manager, Shell


app = create_app(config_name='config')
manager = Manager(app=app)


def make_shell_context():
    return dict(app=app)


# 增加shell命令
manager.add_command('shell', Shell(make_context=make_shell_context))


# 单元测试部分代码
@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()

