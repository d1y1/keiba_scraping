# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

# ここは引数にしたい。
race_url = 'http://race.sp.netkeiba.com/?pid=shutuba&race_id=201806010711'


def crawling(url):
    '''
    URLを指定することでページソースを取得します。
    '''
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r = BeautifulSoup(r.content, 'lxml')
    return r


def get_text(class_name):
    '''
    クラス名を指定すること。
    クラス内のaタグのテキストをリストとしてreturn。
    (※汎用的に使用できるようにしたい。)
    '''
    list = []
    class_name += ' > a'
    row_list = race_row_data.select(class_name)
    for row in row_list:
        i = row.get_text()
        i = i.lstrip(' ').rstrip('\xa0')
        list.append(i)
    return list


if __name__ == '__main__':
# 本レースデータの取得
    race_data = {}
    race_row_data = crawling(race_url)
    race_data['num'] = race_row_data.find(attrs={"class": "Race_Num"}).text.lstrip().rstrip()
    race_data['name'] = race_row_data.find(attrs={"class": "Race_Name"}).text.rstrip()
    course_data = race_row_data.find(attrs={"class": "Race_Data"}).span.text.rstrip()
    race_data['range'] = re.search('\d+.', course_data).group()
    race_data['type'] = re.search('(芝|ダート)', course_data).group()
    # 出場馬のリスト
    horse_list = get_text('.Horse')
    # 出場馬とリンクのディクショナリー
    horse_link = []
    horse_row_link_list = race_row_data.find_all(attrs={"class": "Horse"})
    for row in horse_row_link_list:
        href = row.a.get('href')
        horse_link.append(href)
    horse_url_dict = dict(zip(horse_list, horse_link))
    
    print('レース情報:')
    print(race_data)
    print('出走馬:')
    print(horse_list)
    print(horse_link)
    print(horse_url_dict)
