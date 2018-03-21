#!/usr/bin/env Python
#coding:utf-8
"""
the url structure of website
"""


from learn_tornado.handlers.index import IndexHandler    #假设已经有了

url = [
    (r'/', IndexHandler),
]