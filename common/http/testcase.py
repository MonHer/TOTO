# -*- encoding: utf-8 -*-
"""
@File    : testcase.py
@Time    : 2021/5/23 0023 21:56
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import requests
from common.http.utils import parse_content


class TestCase(object):

    @staticmethod
    def create_session():
        """ create new HTTP session
        """
        return requests.sessions.Session()

    @staticmethod
    def parse_body(content, kwargs):
        return parse_content(content, kwargs)

    def run_test(self):
        """ run_test should be overrided.
        """
        raise NotImplementedError
