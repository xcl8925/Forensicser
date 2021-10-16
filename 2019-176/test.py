import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree
import pandas as pd

data = [
    {
        "children": [
            {"name": "B\nB\nB"},
            {
                "children": [
                    {"children": [{"name": "I"}], "name": "E"},
                    {"name": "F"},
                ],
                "name": "C",
            },
            {
                "children": [
                    {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                    {"name": "H"},
                ],
                "name": "D",
            },
        ],
        "name": "A",
    }
]

print(type(data))
tree = (
    Tree().add("", data, orient="TB").set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
)

tree.render()

df = pd.DataFrame({'key': ['a', 'b', 'c'], 'data1': [1, 2, 3], 'data2': [4, 5, 6]}, index=['x', 'y', 'z'])
print(df)
# for idx, item in df.iterrows():
#     print(idx)
#     print(item)
print(df['key'])
print('\n')
print('\n')

data = df[df['key'].isin(['b'])]
# print(data.index.tolist())
print(data)
print(data.index.tolist()[0])
# print()
print('\n')
print(type(data.loc['y']))
print(data.loc['y']['key'])

print(type(data['key']))
print(data['key'])
print(data['key'][0])


def convert_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.as_dict())
        obj_arr.append(dict)
    return obj_arr


class Test:
    def __init__(self, children=None, name=''):
        if children is None:
            children = []
        self.name = name
        self.children = children

    def as_dict(self):
        obj_arr = []
        for o in self.children:
            obj_arr.append(o.as_dict())
        return {'children': obj_arr, 'name': self.name}


child = Test(name='child')
test = Test([child], 'test')
print(test)
print(test.as_dict())
ar = []
ar.append(test)
ar.append(test)
print(convert_to_dicts(ar))
