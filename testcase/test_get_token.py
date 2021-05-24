# -*- encoding: utf-8 -*-
"""
@File    : test_get_token.py
@Time    : 2021/5/24 0024 23:41
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

from api.GetToken import GetToken
from common.log.logger import logger
from common.http.testcase import TestCase


class TestGetToken(TestCase):
    def test_token(self):
        token = GetToken()\
            .config_verify(True)\
            .set_body({"log": ""})\
            .run()\
            .get_response_object()\
            .json()
        assert token["code"] == "0000000"
        logger.info(token)