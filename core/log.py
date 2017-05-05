"""
@version: 2.0
@author: itacajsj
@license: Apache Licence 
@contact: itacajsj@outlook.com
@site: http://blog.waves-breaker.com
@software: PyCharm
@file: log.py
@time: 2017/5/4 20:52
"""

import logging
import sys

logging.addLevelName(9, "*")
logging.addLevelName(8, "+")
logging.addLevelName(7, "-")
logging.addLevelName(6, "!")

LOGGER = logging.getLogger("KingoLog")

LOGGER_HANDLER = None
