# -*- coding:utf-8 -*-
import os

import pandas
from bs4 import BeautifulSoup  # 网页解析

from models import UserVerifyInfo
from util import get_files


def parse_user_verify_files():
    files = get_files("E:/取证/05.案件支持/上海/青浦反诈/dibaqu/第八区/实名认证", [])
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
        dest_file = '实名认证列表.xlsx'
    else:
        dest_file = 'result/' + str(os.path.basename(file)).split('.')[0] + '.xlsx'

    data.columns = ['UID', '真实姓名', '地址', '身份证号', '正面', '背面', '手持']
    data[["UID"]] = data[["UID"]].astype('int32')
    data.to_excel(dest_file, sheet_name="实名认证列表", index=False, header=True)
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
                    # UID
                    uid = int(tds[0].string.strip())
                    real_name = tds[1].string.strip() if tds[1].string is not None else ''
                    location = tds[4].string.strip() if tds[4].string is not None else ''
                    id_card = tds[5].input.attrs['value'] if tds[5].input is not None else ''
                    front = tds[6].a.attrs['href'].strip()
                    back = tds[6].a.attrs['href'].strip()
                    handle = tds[6].a.attrs['href'].strip()

                    user_info = UserVerifyInfo(uid=uid, real_name=real_name, location=location, id_card=id_card,
                                               front=front,
                                               back=back,
                                               handle=handle)
                    # print(app_info)
                    user_infos.append(user_info)


def main():
    user_infos = parse_user_verify_files()
    write_to_user_excel(user_infos=user_infos)


if __name__ == "__main__":
    main()
    print("success")
