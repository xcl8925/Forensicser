import os


def get_files(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            get_files(cur_path, all_files)
        else:

            all_files.append(cur_path)

    return all_files


# # 传入空的list接收文件名
# contents = get_files("E:/取证/05.案件支持/上海/青浦反诈/dibaqu/第八区/", [])
# # 循环打印show_files函数返回的文件名列表
# for content in contents:
#     print(content)
