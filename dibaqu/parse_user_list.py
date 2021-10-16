# -*- coding:utf-8 -*-
import os

import pandas
from bs4 import BeautifulSoup  # 网页解析

from dibaqu.models import UserInfo
from dibaqu.util import get_files


def parse_user_files():
    files = get_files("E:/取证/05.案件支持/上海/青浦反诈/dibaqu/第八区/用户管理", [])
    # 循环打印get_files函数返回的文件名列表
    count = 0
    user_infos = []
    for file in sorted(files):
        # if file.find('1414.html') > 0:
        print(file)
        count = count + 1
        print(count)
        parse_html(file, user_infos)
        # write_to_excel(file, app_infos)

    return user_infos


def write_to_user_excel(file='', user_infos=None):
    if user_infos is None:
        app_infos = []
    data = pandas.DataFrame([app_info.as_dict() for app_info in user_infos])
    if file == '':
        dest_file = '用户列表.xlsx'
    else:
        dest_file = 'result/' + str(os.path.basename(file)).split('.')[0] + '.xlsx'

    data.columns = ['UID', '用户名', 'APP数量', '登录IP', '最后登录时间', '注册时间']
    data[["UID"]] = data[["UID"]].astype('int32')
    data[["APP数量"]] = data[["APP数量"]].astype('int32')
    data.to_excel(dest_file, sheet_name="用户列表", index=False, header=True)
    # if os.path.exists(dest_file):
    #     exist_data = pandas.read_excel(dest_file)
    #     exist_data.append(data)
    #     exist_data.to_excel(dest_file, sheet_name="封装列表", index=False, header=True)
    # else:
    #     pass


# 解析html
def parse_html(file, user_infos):
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
                    uid = int(tds[0].string.strip())
                    user_name = tds[1].a.string.strip() if tds[1].a.string is not None else ''
                    count = int(tds[4].a.string.strip())
                    login_ip = tds[5].string.strip() if tds[5].string is not None else ''
                    last_login_time = tds[6].string.strip()
                    register_time = tds[7].string.strip()

                    user_info = UserInfo(uid=uid, user_name=user_name, count=count, login_ip=login_ip,
                                         last_login_time=last_login_time,
                                         register_time=register_time)
                    # print(app_info)
                    user_infos.append(user_info)


def main():
    user_infos = parse_user_files()
    write_to_user_excel(user_infos=user_infos)


if __name__ == "__main__":
    main()
    print("success")
