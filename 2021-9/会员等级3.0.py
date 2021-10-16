from collections import Counter
from time import sleep
import time

filedic = {}
filedic_sort = {}
filedic_level = {}
filedic_name = {}
filedic_up = {}
pidlist = []


def openfile():
    filelist = []
    file = open("user_cal.txt", 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            break
        filelist.append(line.strip('\n').split('\t'))
    return filelist


def create_filedic():
    filelist = openfile()
    for fl in filelist:
        # id-pid
        filedic[fl[0]] = fl[3]
        # id-level
        filedic_level[fl[0]] = fl[2]
        # id-name
        filedic_name[fl[0]] = fl[1]
    for k, v in filedic.items():
        # pid-ids
        filedic_sort.setdefault(v, []).append(k)
    list = []
    for key, value in filedic_level.items():
        # levels
        list.append(value)


def get_all_children(pids_counter, id, level, down_ids):
    # print("id:"+str(id))
    if id in pids_counter.keys():
        level += 1
        # print("level:" + str(level))
        for j in filedic_sort[id]:
            down_ids.append(j)
            level, down_ids = get_all_children(pids_counter, j, level, down_ids)
        return level, down_ids
    else:
        return level, down_ids


def user_level():
    create_filedic()
    print("全部字典接收成功，开始处理...")
    sleep(3)
    # pids
    for pid in filedic.values():
        pidlist.append(pid)
    pids_counter = Counter(pidlist)
    for id, pid in filedic.items():
        if int(id) == 0:
            continue
        if id in pids_counter.keys():
            level, down_ids = get_all_children(pids_counter, id, 1, [])

            down_name = []
            down_down_id = []
            down_down_name = []
            for inner_id in filedic_sort[id]:
                down_name.append(filedic_name[inner_id])
                if inner_id in pids_counter.keys():
                    for j in filedic_sort[inner_id]:
                        down_down_id.append(j)
                        down_down_name.append(filedic_name[j])
            if id in filedic_name.keys():
                text = "id[{},{}]当前层级为{}".format(id, filedic_name[id], filedic_level[id]) + \
                       '    ' + "推荐人id[{}]".format(pid) + \
                       '    ' + "三层发展总人数{}".format(len(down_down_id) + int(pids_counter[id]) + 1) + \
                       '    ' + "下級層級{}".format(level) + \
                       '    ' + "总下级人数{}".format(len(down_ids) + 1)

                with open("存在直属下级.txt", 'a', encoding='utf-8') as f:
                    f.write(text + '\n')
                print(text)
        # else:
        #     text = "id[{},{}]当前层级为{}".format(id,filedic_name[id],filedic_level[id])+"推荐人id[{}]".format(pid)+\
        #            '    '+"推荐人用户名{}".format(filedic_name[pid])+'    '+"直属下级数为0"
        #     with open("无直属下级.txt",'a',encoding='utf-8') as f:
        #         f.write(text+'\n')


if __name__ == "__main__":
    start_time = time.time()
    user_level()
    print("总用时：{}".format(time.time() - start_time))
