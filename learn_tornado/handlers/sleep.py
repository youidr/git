#!/usr/bin/env Python
#coding:utf-8

import tornado.web
import tornado.ioloop
from learn_tornado.handlers.base import BaseHandler
import time
import tornado.gen

class SleepHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)

    def on_response(self):
        self.render("sleep.html")
        return

class SeeHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 10)
        self.render("see.html")