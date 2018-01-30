#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
from modules import *


@route('/static/css/<filename:re:.*\.less>')
def css(filename):
    return static_file(filename, root="static/css")


# localhost:8080/check
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
    
    if tag:
        data = data.find_all(tag)
        if word:
            r = re.compile(word)
            data = list(data)
            data = [x for x in data if r.match(x)]

    # View部 =============================================
    # views/check.tplを呼ぶ
    return template('check_result', data=data)


# ビルドインサーバの実行 ========================================
run(host='d1y1.net', port=8080, debug=True, reloader=True)
