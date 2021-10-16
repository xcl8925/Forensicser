import requests
import json
import time


def send(method, url, headers, params='', data='', cookies=''):
    if method.lower() == "get":
        res = requests.get(url, headers=headers, params=params, verify=False, cookies=cookies)
        return res
    elif method.lower() == "post":
        if len(params) > 0:
            res = requests.post(url, headers=headers, params=params, data=data.encode("utf-8"), verify=False,
                                cookies=cookies)
        else:
            res = requests.post(url, headers=headers, data=data.encode("utf-8"), verify=False, cookies=cookies)
        return res
    elif method.lower() == "put":
        if params is not None:
            res = requests.put(url, headers=headers, data=data.encode("utf-8"), verify=False)
        else:
            res = requests.put(url, verify=False)
        return res

    elif method.lower() == "delete":
        if params is not None:
            res = requests.delete(url, hearders=headers, data=data.encode("utf-8"), verify=False)
        else:
            res = requests.put(url, hearders=headers, verify=False)
        return res
    else:
        print("无效的请求方式，get/post/put/delete,请查找原因！！！")


def login():
    payload = "dosubmit=yes&username=admin&password=Ghy511&submit.x=26&submit.y=17"
    url = "http://crm.joysw.cn/login.php"
    headers = {
        "Host": "crm.joysw.cn",
        "Connection": "keep-alive",
        "Content-Length": "67",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://crm.joysw.cn",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, " \
                      "like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://crm.joysw.cn/login.php",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    res = send(url=url, method="post", headers=headers, data=payload)
    cookies = res.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    return cookie


def start(id):
    getcookie = {"PHPSESSID": "n2l0nr399ob9caaef6hu7furef", "admin_token": "%2BS9anoA0Ja7%2FPtpwb2VxAQ%3D%3D"}

    headers = {
        "Host": "dibaqu.com",
        "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://dibaqu.com/admin/pack",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    while id <= 75:
        strid = str(id)
        url = "https://dibaqu.com/admin/withdraw?page={id}".format(id=strid)
        # data = "pageNow={id}&pageSize=10&zone=md&state=&site=&parentName=&" \
        # 	   "begintime=2015-10-16+00%3A00%3A00&endtime=2020-10-16+23%3A59%3A59&" \
        # 	   "username=&timetype=submitTime&vipLevelId=&serialid=&paychannel=&beginAmount=&endAmount=".format(
        # 	id=id)
        workres = send(method="GET", url=url, headers=headers, cookies=getcookie)
        filrename = strid
        with open("E:\\dibaqu\\提现记录\\%s.html" % filrename, "w", encoding="utf-8") as f:
            f.write(workres.text)
        id = id + 1


if __name__ == "__main__":
    id = 1
    start(id)
