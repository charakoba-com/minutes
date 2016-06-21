#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle, redirect, request, response
from functools import wraps
import xml.sax.saxutils as html
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



def params(require=[], option=[]):
    def wrap(func):
        @wraps(func)
        def _(*a, **ka):
            parameter = {}
            for key in require:
                if key in request.forms:
                    parameter[key] = request.forms.get(key)
                else:
                    response.status = 400
                    return {
                        'status': False,
                        'message': '{} is required.'.format(key)
                    }
            for key in option:
                if key in request.forms:
                    parameter[key] = request.forms.get(key)
            return func(parameter, *a, **ka)
        return _
    return wrap


@get('/api/report/list')
def api_get_report_list():
    response.set_header('Access-Control-Allow-Origin', '*')
    with DB.connect(cursorclass=DC, **cfg['DB_INFO']) as cursor:
        query = 'SELECT * FROM reports;'
        cursor.execute(query)
        rows = cursor.fetchall()
    done = []
    list_ = []
    for row in rows:
        key = str(row['year']) + '/' + str(row['month']) + '/' + str(row['week'])
        if key in done:
            continue
        else:
            list_.append(
                {
                    'key': key,
                }
            )
    return {'list': list_}


@get('/api/report/<year:int>/<month:int>/<week:int>')
def api_get_report(year, month, week):
    response.set_header('Access-Control-Allow-Origin', '*')
    with DB.connect(cursorclass=DC, **cfg['DB_INFO']) as cursor:
        query = 'SELECT * FROM reports WHERE year=%s AND month=%s AND week=%s;'
        cursor.execute(
            query,
            (year, month, week)
        )
        rows = cursor.fetchall()
    reports = []
    for row in rows:
        reports.append(
            {
            "username": row['username'],
            "body": html.escape(row['body'])
            }
        )
    return {'reports': reports}


@post('/api/report/<year:int>/<month:int>/<week:int>')
@params(['username', 'body'])
def api_post_report(parameter, year, month, week):
    response.set_header('Access-Control-Allow-Origin', '*')
    username = parameter['username']
    body = parameter['body']
    with DB.connect(cursorclass=DC, **cfg['DB_INFO']) as cursor:
        query = 'INSERT INTO reports VALUES(%s, %s, %s, %s, %s);'
        cursor.execute(
            query,
            (username, year, month, week, body)
        )
    return {"status": True}
