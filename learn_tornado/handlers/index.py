#!/usr/bin/env Python
#coding:utf-8

import tornado.web
from learn_tornado.methods.db import *
from .base import BaseHandler
import tornado.escape


class IndexHandler(BaseHandler):
    def get(self):
        usernames = select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome you: " + username)
                #self.set_cookie(username, db_pwd)
                self.set_current_user(username)  # 将当前用户名写入 cookie，方法见下面
                self.write(username)
            else:
                self.write("-1")
        else:
            self.write("-1")


    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))  # 注意这里使用了 tornado.escape.json_encode() 方法
        else:
            self.clear_cookie("user")


class ErrorHandler(BaseHandler):  # 增加了一个专门用来显示错误的页面
    def get(self):  # 但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")


