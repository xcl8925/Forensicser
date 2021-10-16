import requests


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
    payload = "{\"tenantId\":null,\"paymentType\":null,\"page\":1,\"pageSize\":10,\"accountType\":\"CASH\"," \
              "\"start\":null,\"end\":null}"
    url = "http://os.lwork.com/v1/ops/tenants/payment"
    headers = {
        "Host": "os.lwork.com",
        "Proxy-Connection": "keep-alive",
        "Content-Length": "104",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://os.lwork.com",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4350.7 Safari/537.36",
        "Accept": "*/*",
        "Referer": "http://os.lwork.com/static/view/system/payment/view.html",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "X-Requested-With",
        "X-Api-Token": "PUB:T001OPS:73be9187-580e-48f6-8e6d-de6aae59fc49:a0c44988-d58f-46dd-abba-a89070418b0a",
        "X-Language": "zh-CN",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6"
    }
    res = send(url=url, method="POST", headers=headers, data=payload)
    with open("E:\\1.json", "w", encoding="utf-8") as f:
        f.write(res.text)


def detail():
    payload = "{\"tenantId\":null,\"paymentType\":null,\"page\":1,\"pageSize\":10,\"accountType\":\"CASH\"," \
              "\"start\":null,\"end\":null}"
    url = "http://os.lwork.com/v1/ops/tenants/list"
    headers = {
        "Host": "os.lwork.com",
        "Proxy-Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4350.7 Safari/537.36",
        "Accept": "*/*",
        "Referer": "http://os.lwork.com/static/view/system/payment/view.html",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "X-Requested-With",
        "X-Api-Token": "PUB:T001OPS:73be9187-580e-48f6-8e6d-de6aae59fc49:a0c44988-d58f-46dd-abba-a89070418b0a",
        "X-Language": "zh-CN",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6"
    }
    res = send(url=url, method="get", headers=headers)
    with open("E:\\1.json", "w", encoding="utf-8") as f:
        f.write(res.text)


def start(id):
    getcookie = {"JSESSIONID": "BD2C9888DBE01A65148379B5929E88C7"}

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
    # detail()

    headers = {
        "Host": "os.lwork.com",
        "Proxy-Connection": "keep-alive",
        "Content-Length": "104",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://os.lwork.com",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4350.7 Safari/537.36",
        "Accept": "*/*",
        "Referer": "http://os.lwork.com/static/view/system/payment/view.html",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "X-Requested-With",
        "X-Api-Token": "PUB:T001OPS:73be9187-580e-48f6-8e6d-de6aae59fc49:a0c44988-d58f-46dd-abba-a89070418b0a",
        "X-Language": "zh-CN",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6"
    }

    print(type(headers))

    print(headers)
    headers = {}
    with open("F:\\workspace\\python\\Forensicser\\lwork\\data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip()
            splits = data.split(':')
            if len(splits) > 1:
                headers[splits[0]] = splits[1].strip()

    print(headers)
