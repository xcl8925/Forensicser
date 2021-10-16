# -*- coding: utf-8 -*-
import subprocess
import re


def python_call_powershell(address):
    try:
        args = [r"powershell", r"C:\Users\Panguite\Desktop\a.ps1", address]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()  # 这里是标准输出，也就是PowerShell输出什么都会被传递这里输出
        return dt
    except Exception as e:
        print(e)
    return False


if __name__ == "__main__":
    # ip = ["blog.bigyoung.cn", "blog.bigyoung.cn0", "3.3.3.3"]
    ip = 'C:\\Users\\Panguite\\Desktop\\a.dll'  # 这里定义的IPlist 需要是一个str类型
    # print python_call_powershell(",".join(ip))
    # ip = re.split(":",ip)
    # print(python_call_powershell(ip))
    print(python_call_powershell(ip)[29:47])
