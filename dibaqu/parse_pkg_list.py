# -*- coding:utf-8 -*-
import os
import sys
from bs4 import BeautifulSoup  # 网页解析
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 获取指定url网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import lxml
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

from dibaqu.models import AppInfo
import pandas
from dibaqu.util import get_files


def parse_pkg_files():
    files = get_files("E:/取证/05.案件支持/上海/青浦反诈/dibaqu/第八区/封装列表", [])
    # 循环打印get_files函数返回的文件名列表
    count = 0
    app_infos = []
    for file in sorted(files):
        # if file.find('1414.html') > 0:
        # print(file)
        count = count + 1
        print(count)
        parse_pkg_html(file, app_infos)
        # write_to_excel(file, app_infos)
    return app_infos


def write_to_excel(file='', app_infos=None):
    if app_infos is None:
        app_infos = []
    data = pandas.DataFrame([app_info.as_dict() for app_info in app_infos])
    if file == '':
        dest_file = '封装列表.xlsx'
    else:
        dest_file = 'result/' + str(os.path.basename(file)).split('.')[0] + '.xlsx'

    data.columns = ['编号', 'UID', '应用名称', '封装地址', '创建时间', '到期时间', '分发链接']
    # data[["编号"]] = data[["编号"]].astype(str)
    data.to_excel(dest_file, sheet_name="封装列表", index=False, header=True)
    # if os.path.exists(dest_file):
    #     exist_data = pandas.read_excel(dest_file)
    #     exist_data.append(data)
    #     exist_data.to_excel(dest_file, sheet_name="封装列表", index=False, header=True)
    # else:
    #     pass


# 解析html
def parse_pkg_html(file, app_infos):
    # html.parser是解析器，也可是lxml
    soup = BeautifulSoup(open(file, encoding='utf-8'), features='html.parser',
                         from_encoding='UTF-8')
    table = soup.table
    if table is not None:
        # tbody节点
        tbody = table.tbody
        if tbody is not None:
            # tr节点
            for tr in tbody.find_all('tr'):
                # td节点
                tds = tr.find_all('td')
                if len(tds) > 1:
                    # UID
                    app_id = str(str(tds[0]).split('<br', 1)[0].split('">', 1)[1].strip())
                    uid = int(str(tds[1].a.string).strip())
                    name = str(tds[2].a.contents[2].replace('[', '')).strip()
                    domain = tds[2].a.attrs['href'].strip()
                    domain = ILLEGAL_CHARACTERS_RE.sub(r'', domain)
                    create_time = str(tds[3].string).strip()

                    if tds[4].string is None:
                        end_time = str(tds[4].font.string).strip()
                    else:
                        end_time = str(tds[4].string).strip()

                    if tds[5].a is None:
                        delivery = ''
                    else:
                        delivery = str(tds[5].a.string).strip()

                    app_info = AppInfo(app_id=app_id, uid=uid, name=name, domain=domain, create_time=create_time,
                                       end_time=end_time, delivery=delivery)
                    # print(app_info)
                    app_infos.append(app_info)


def main():
    app_infos = parse_pkg_files()
    write_to_excel(app_infos=app_infos)
    print("success")


if __name__ == "__main__":
    main()
