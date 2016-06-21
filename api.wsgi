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


@get('/report/<year:int>/<month:int>/<week:int>')
def api_get_report(year, month, week):
    pass


@post('/report/<year:int>/<month:int>/<week:int>')
def api_post_report(year, month, week):
    pass
