#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from modules import *

# localhost:8080
@route('/check')
def title():
    # views/check.tplを呼ぶ
    return template('check')


# localhost:8080/show
@route('/check', method='GET')
def men():
    # GETパラメータの取得 =====================================
    race_url = request.query.url

    # Controller部 =======================================
    data = scraping.crawling(race_url)
    
    # View部 =============================================
    # views/check.tplを呼ぶ
    return template('check', data=data)


# ビルドインサーバの実行 ========================================
run(host='d1y1.net', port=8080, debug=True, reloader=True)
