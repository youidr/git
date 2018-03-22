#!/usr/bin/env Python
#coding:utf-8

from learn_tornado.url import url
import tornado.web
import os

settings = {
    'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    'static_path' : os.path.join(os.path.dirname(__file__), "static"),
    'debug' : True,
    'cookie_secret' : "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    'xsrf_cookies' : True,
    'login_url' : '/',
}

application = tornado.web.Application(handlers = url,**settings)