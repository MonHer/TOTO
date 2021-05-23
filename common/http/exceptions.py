# -*- encoding: utf-8 -*-
"""
@File    : exceptions.py
@Time    : 2021/5/23 0023 21:05
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import json

JSONDecodeError = json.JSONDecodeError

""" failure type exceptions
    these exceptions will mark test as failure
"""


class MyBaseFailure(Exception):
    pass


class ExtractFailure(MyBaseFailure):
    pass


""" error type exceptions
    these exceptions will mark test as error
"""


class MyBaseError(Exception):
    pass


class ParamsError(MyBaseError):
    pass
