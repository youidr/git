#!/usr/bin/env Python
#coding:utf-8
"""
the url structure of website
"""


from learn_tornado.handlers.index import IndexHandler    #假设已经有了
from learn_tornado.handlers.user import UserHandler
from learn_tornado.handlers.sleep import *


url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/see', SeeHandler),
    (r'/sleep', SleepHandler),
]