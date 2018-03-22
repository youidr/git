#!/usr/bin/env Python
#coding:utf-8
import tornado.web
import tornado.escape
from learn_tornado.methods.db import *
from learn_tornado.handlers.base import BaseHandler

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = tornado.escape.json_decode(self.current_user)
        user_infos = select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", users=user_infos)
