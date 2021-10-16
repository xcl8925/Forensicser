# -*- coding:utf-8 -*-

import sys
from bs4 import BeautifulSoup  # 网页解析
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 获取指定url网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)

    # 3.保存数据
    savepath = "豆瓣电影.xls"
    saveData(datalist, savepath)


# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')


def getData(baseurl):
    datalist = []

    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item)
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]  # 用re库通过正则查找指定的链接
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')

            datalist.append(data)  # 把处理好的一部电影信息放入datalist
    # print(datalist)
    return datalist


def askURL(url):
    head = {
        # 用户代理，告诉服务器我们试用的浏览器类型，本质上是告诉服务器我们可以接收什么水平的内容
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('sheet001', cell_overwrite_ok=True)
    col = ("电影详情页", "电影图片", "电影中文名", "英文名")
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 4):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)


if __name__ == "__main__":
    main()
    print("输出完了")
