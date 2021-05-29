# -*- encoding: utf-8 -*-
"""
@File    : test_get_token.py
@Time    : 2021/5/24 0024 23:41
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import allure
from api.GetToken import GetToken
from common.log.logger import logger
from common.http.testcase import TestCase


@allure.feature("网关验证功能")
class TestGetToken(TestCase):
    @allure.story("测试获取token")
    def test_token(self):
        with allure.step("测试获取token"):
            token = GetToken() \
                .config_verify(True) \
                .set_body({"log": ""}) \
                .run() \
                .get_response_object() \
                .json()
            assert token["code"] == "0000000"
            allure.attach(str(token), str(token))
            logger.info(token)
