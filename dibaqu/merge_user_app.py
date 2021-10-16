# 将用户信息添加进应用列表信息中
import os
import sys

import pandas

from dibaqu.parse_pkg_list import parse_pkg_files
from dibaqu.parse_user_list import parse_user_files
import dibaqu.models
from dibaqu.models import AppUserInfo


def main():
    # 读取应用，用户列表
    app_infos = parse_pkg_files()
    user_infos = parse_user_files()

    app_user_infos = []
    count = 0
    for app_info in app_infos:
        app_user_info = AppUserInfo()
        app_user_info.app_info = app_info
        for user_info in user_infos:
            if app_info.uid == user_info.uid:
                app_user_info.user_info = user_info
                break
        app_user_infos.append(app_user_info)
        print(app_user_info.as_dict().__str__())
        count += 1
        print(count)
    write_to_excel(app_user_infos=app_user_infos)


def write_to_excel(file='', app_user_infos=None):
    if app_user_infos is None:
        app_infos = []
    data = pandas.DataFrame([app_info.as_dict() for app_info in app_user_infos])
    if file == '':
        dest_file = '用户应用列表.xlsx'
    else:
        dest_file = 'result/' + str(os.path.basename(file)).split('.')[0] + '.xlsx'

    data.columns = ['编号', 'UID', '应用名称', '封装地址', '创建时间', '到期时间', '分发链接',
                    '用户名', 'APP数量', '登录IP', '最后登录时间', '注册时间']
    # data[["UID"]] = data[["UID"]].astype('int32')
    # data[["APP数量"]] = data[["APP数量"]].astype('int32')
    data.to_excel(dest_file, sheet_name="用户应用列表", index=False, header=True)
    # if os.path.exists(dest_file):
    #     exist_data = pandas.read_excel(dest_file)
    #     exist_data.append(data)
    #     exist_data.to_excel(dest_file, sheet_name="封装列表", index=False, header=True)
    # else:
    #     pass


if __name__ == '__main__':
    sys.stdout = open("stdout.txt", mode="a")
    main()
