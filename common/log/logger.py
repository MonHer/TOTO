# -*- encoding: utf-8 -*-
"""
@File    : logger.py
@Time    : 2021/5/29 0029 22:37
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import os
import time
import logging
from pathlib import Path

# BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_PATH = Path().absolute()
# 定义log文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
print(LOG_PATH)
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:
    def __init__(self):
        self.LogName = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d%H%M%S")))
        self.LogGer = logging.getLogger("log")
        self.LogGer.setLevel(logging.DEBUG)
        self.FoMmaTer = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        self.FileLogGer = logging.FileHandler(self.LogName, mode="a", encoding="UTF-8")
        self.ConSole = logging.StreamHandler()
        self.ConSole.setLevel(logging.DEBUG)
        self.FileLogGer.setLevel(logging.DEBUG)
        self.FileLogGer.setFormatter(self.FoMmaTer)
        self.ConSole.setFormatter(self.FoMmaTer)
        self.LogGer.addHandler(self.FileLogGer)
        self.LogGer.addHandler(self.ConSole)


logger = Logger().LogGer

if __name__ == "__main__":
    logger.info("--测试开始--")
    # logger.info()
    logger.info(LOG_PATH)
    logger.debug("--测试结束--")