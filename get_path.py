# -*- encoding: utf-8 -*-
"""
@File    : get_path.py
@Time    : 2021/5/30 0030 23:50
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

from pathlib import Path


class HomePath(object):
    @staticmethod
    def get_path():
        return Path.cwd()


home_path = HomePath.get_path()