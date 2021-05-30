# -*- encoding: utf-8 -*-
"""
@File    : test_dome.py
@Time    : 2021/5/30 0030 0:43
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import allure


@allure.feature("添加allure")
class TestAllure(object):
    @allure.story("测试allure")
    def test_add_allure(self):
        with allure.step("求和"):
            ss = 3 + 5
            allure.attach(str(ss), ss)
        with allure.step("求差"):
            sss = 5 - 1
            allure.attach(str(sss), sss)

        with allure.step("取模"):
            d = 500 % 128
            allure.attach(str(d), d)
