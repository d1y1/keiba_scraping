#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from modules import *

# localhost:8080
@route('/check')
def title():
    # views/check.tplを呼ぶ
    data = 0
    return template('check')


# localhost:8080/show
@route('/check_result', method='GET')
def men():
    # GETパラメータの取得 =====================================
    url = request.query.url
    tag = request.query.tag
    word = request.query.word

    # Controller部 =======================================
    data = scraping.crawling(url)
    
    if word and tag:
        data = data.find_all(tag, text=re.compile(word))

    # View部 =============================================
    # views/check.tplを呼ぶ
    return template('check_result', data=data)


# ビルドインサーバの実行 ========================================
run(host='d1y1.net', port=8080, debug=True, reloader=True)
