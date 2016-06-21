#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle, redirect, request, response
from functools import wraps
import json
import MySQLdb as DB
from MySQLdb.cursors import DictCursor as DC

with open('config.json', 'r') as f:
    cfg = json.load(f)

app = application = Bottle()
get = app.get
post = app.post
put = app.put
delete = app.delete

def session(func=None):
    @wraps
    def _(*a, **ka):
        sessid = request.get_cookie('sessid')
        if sessid:
            query = 'SELECT * FORM session WHERE session_id=%s;'
            with DB.connect(cursorclass=DC, **cfg['DB_INFO']) as c:
                c.execute(query, (sessid,))
                row = c.fetchone()
            if row:
                return func(*a, **ka)
            else:
                redirect(cfg['LOGIN_PAGE'])
    return _
