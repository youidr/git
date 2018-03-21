#!/usr/bin/env Python
#coding:utf-8

import tornado.web
from learn_tornado.methods.db import *

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")

