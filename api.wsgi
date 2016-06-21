#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle, request, response
import json

with open('config.json', 'r') as f:
    cfg = json.load(f)

app = application = Bottle()
get = app.get
post = app.post
put = app.put
delete = app.delete
