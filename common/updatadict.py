# -*- encoding: utf-8 -*-
"""
@File    : updatadict.py
@Time    : 2021/5/24 0024 23:09
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""


def update_json(my_dict, key, value):
    if isinstance(my_dict, dict):  # 使用isinstance检测数据类型，如果是字典
        if key in my_dict.keys():  # 替换字典第一层中所有key与传参一致的key
            my_dict[key] = value
        for k in my_dict.keys():  # 遍历字典的所有子层级，将子层级赋值为变量chdict，分别替换子层级第一层中所有key对应的value，最后在把替换后的子层级赋值给当前处理的key
            chdict = my_dict[k]
            update_json(chdict, key, value)
            my_dict[k] = chdict
    elif isinstance(my_dict, list):  # 如是list
        for element in my_dict:  # 遍历list元素，以下重复上面的操作
            if isinstance(element, dict):
                if key in element.keys():
                    element[key] = value
                for k in element.keys():
                    chdict = element[k]
                    update_json(chdict, key, value)
                    element[k] = chdict
