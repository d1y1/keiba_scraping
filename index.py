#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from modules import *

# localhost:8080
@route('/')
def title():
    # views/title.tplを呼ぶ
    return template('title')


# localhost:8080/show
@route('/show', method='GET')
def men():
    # GETパラメータの取得(username, men)
    race_url = request.query.url

    # Controller部 =======================================
    data = scraping.crawling(race_url)
    
    
    # View部 =============================================
    # views/show.tplを呼ぶ
    return template('show', data=data)


# ビルドインサーバの実行
run(host='d1y1.net', port=8080, debug=True, reloader=True)
