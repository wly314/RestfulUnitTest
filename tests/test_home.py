#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140137128705556022982cfd844b38d050add8565dcb9000
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
比如对函数abs()，我们可以编写出以下几个测试用例：
    输入正数，比如1、1.2、0.99，期待返回值与输入相同；
    输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
    输入0，期待返回0；
    输入非数值类型，比如None、[]、{}，期待抛出TypeError。
把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。
单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
"""
from test_basic import BasicTestCase


class HomeTest(BasicTestCase):
    def test_home_get(self):
        response = self.client.get('/v1/home?name={}'.format('test'))
        print 'test_home_page:' + response.data

    def test_home_delete(self):
        data = {
            'user_id': '1'
        }
        response = self.client.delete('/v1/home', data=data)
        data = response.get_data(as_text=True)
        print 'test_home_page:' + data
        self.assertTrue('buy-buy' in data)

        data2 = {
            'user_id': 'test'
        }
        response2 = self.client.delete('/v1/home', data=data2)
        data = response2.data
        print 'test_home_page:' + data
        self.assertTrue('buy-buy' not in response2.get_data(as_text=True))

