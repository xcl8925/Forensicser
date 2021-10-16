import json

import pandas as pd
from pyecharts.charts import Tree
from pyecharts import options as opts

source_file = r"E:\取证\09.鉴定\盘石鉴定所\鉴定案件\2019-176\光盘-补-3\structure_B\组织架构_B.xlsx"

# source_file = r"E:\取证\09.鉴定\盘石鉴定所\鉴定案件\2019-176\光盘-补-3\structure_A\组织架构_A.xlsx"

ids = []
data = None
account_id = '客户账号'
name = '客户登录名'
card_id = '客户身份证'
lower_ids = '下级人员'


# 身份证号
def read_ids():
    with open(r'F:\workspace\python\Forensicser\2019-176\ids.txt', 'r', encoding='utf-8') as file:
        global ids
        ids = file.readlines()  # 读取所有行并返回列表
        ids = [x.strip() for x in ids]


def read_data():
    global data
    data = pd.read_excel(source_file, sheet_name=0, usecols='A,C,D,G,H,I,J,K')
    # data = data[(data['下属人数'] >= 30) & (data['下属层级数'] >= 8) & data['客户身份证'].isin(ids)]
    # data = data[(data['下属人数'] >= 30) & (data['下属层级数'] >= 3) & data['客户身份证'].isin(ids)]
    data = data[data['客户身份证'].isin(ids)]
    # 根据客户身份证去重
    # data = data.drop_duplicates(subset=['客户身份证'],
    #                             keep='first')
    data.sort_values(by='所在层级', ascending=False, inplace=True)
    print(len(data))
    print(data)
    for index in data.index:
        print(data.loc[index].values)

    parse_data()


def parse_data():
    users = []
    user1 = User(children=None, account_id='MY000001225-1', name='longs001-1', card_id='41082619760103451X')
    values = data.loc[data['客户账号'] == 'MY000001225-1']
    parse_user(user1, values)
    print(user1.as_dict())
    result = [user1.as_dict()]
    tree = (
        Tree().add("", result, orient="TB").set_global_opts(title_opts=opts.TitleOpts(title="层级关系图"))
    )


def parse_user(user=None, values=None):
    print(values[account_id].tolist())
    user.account_id = values[account_id].tolist()[0]
    user.name = values[name].tolist()[0]
    user.card_id = values[card_id].tolist()[0]
    lowers = values[lower_ids].tolist()[0].split(';')
    for lower in lowers:
        temp_user = User()
        lower_values = data.loc[data['客户账号'] == lower]
        if len(lower_values) == 0:
            tree.render()
            pass
        else:
            parse_user(temp_user, lower_values)
            user.children.append(temp_user)


def search_children():
    pass


def main():
    global ids
    read_ids()
    read_data()


class User:
    def __init__(self, children=None, account_id='', name='', card_id=''):
        if children is None:
            children = []
        self.children = children
        self.account_id = account_id
        self.name = name
        self.card_id = card_id

    def as_dict(self):
        obj_arr = []
        for o in self.children:
            obj_arr.append(o.as_dict())
        return {'name': self.name + '\n' + self.account_id, 'card_id': self.card_id, 'children': obj_arr}


if __name__ == '__main__':
    main()
