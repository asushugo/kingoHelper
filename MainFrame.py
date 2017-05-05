# encoding: utf-8


"""
@version: 2.0
@author: itacajsj
@license: Apache Licence 
@contact: itacajsj@outlook.com
@site: http://blog.waves-breaker.com
@software: PyCharm
@file: MainFrame.py
@time: 2017/5/4 20:19

主要逻辑
"""

from configparser import ConfigParser
config=ConfigParser()
config.read('config.conf')

import requests
