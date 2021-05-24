# -*- encoding: utf-8 -*-
"""
@File    : read_file_data.py
@Time    : 2021/5/24 0024 23:02
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import json
import yaml
from pathlib import Path
from common.log.logger import logger
from configparser import ConfigParser


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData(object):

    @staticmethod
    def get_path(file_path):
        current_path = str(Path().absolute().parent)
        logger.info("获取根目录 %s" % current_path)
        path = Path(current_path, file_path)
        logger.info("拼接后的文件地址为 ==>>  {} ".format(path))
        return path

    @staticmethod
    def load_json(file_path):
        path = ReadFileData.get_path(file_path)
        logger.info("加载 {} 文件......".format(path))
        with open(path, "r", encoding="utf-8") as parameter:
            json_data = json.load(parameter)
            logger.info("读到数据 ==>>  {} ".format(json_data))
            return json_data

    @staticmethod
    def load_yaml(file_path):
        path = str(ReadFileData.get_path(file_path))
        logger.info("加载 {} 文件......".format(path))
        with open(path, "r", encoding="utf-8") as ParameterValue:
            yaml_data = yaml.load(ParameterValue.read(), Loader=yaml.Loader)
            logger.info("读到数据 ==>>  {} ".format(yaml_data))
            return yaml_data

    @staticmethod
    def load_ini(file_path):
        path = ReadFileData.get_path(file_path)
        logger.info("加载 {} 文件......".format(path))
        config = MyConfigParser()
        config.read(path, encoding="UTF-8")
        data = dict(config._sections)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data


def main():
    yaml_path = "config/service.yaml"
    json_path = "data/json/merlot/queryContractSignCheckInfo.json"
    print(ReadFileData.load_yaml(yaml_path))
    print(ReadFileData.load_json(json_path))


if __name__ == '__main__':
    main()