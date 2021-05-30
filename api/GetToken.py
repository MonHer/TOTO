# -*- encoding: utf-8 -*-
"""
@File    : GetToken.py
@Time    : 2021/5/24 0024 23:30
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

from common.readfile.read_file_data import ReadFileData
from common.http.request import HttpRequest


class GetToken(HttpRequest):
    __IP = ReadFileData.load_yaml("config/servicer.yaml")
    method = HttpRequest.EnumHttpMethod.POST
    url = __IP["test"]["url"] + "/aiproduct/tokenService/getToken"
    # url = __IP.get("url") + "/aiproduct/tokenService/getToken"
    headers = {"Content-Type": "application/json"}
