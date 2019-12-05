# -*- coding:utf-8 -*-
import random

def get_check_icon_list(path):
    path = path
    attrib_cmd = "attrib -s -h -r " + path + "\\*.* && del " + path + "\\*.* /q"
    dir_cmd = "dir " + path + " /ad /b /s >del.txt"
    to_utf8 = 'PowerShell -Command "& {get-content del.txt -encoding default | set-content del_utf8.txt -encoding utf8}"'
    os.system(attrib_cmd)
    os.system(dir_cmd)
    os.system(to_utf8)
    # add mark to list
    with open('del_utf8.txt', 'r') as f:
        path_list = f.read()
        path_list_space = path_list.split("\n")
        switch_list = []
        for i in path_list_space:
            print(i)
            mark_string = '\"' + i + '\"'
            print(mark_string)
            switch_list.append(mark_string)
    del switch_list[-1]
    print(switch_list)  
    print(len(switch_list))
    # get mark txt file
    with open('del_utf8.txt', 'w') as e:
        for j in switch_list:
            e.write(j)
            e.write('\n')
    # get final list
    with open('del_utf8.txt', 'r') as g:
        mark_data = g.read()
        mark_list = mark_data.split("\n") 
    return mark_list

print(get_check_icon_list(path = "D:\\test"))
"""    
ran_list = random.sample(mark_list, 2)
for i in ran_list:
    type("r", KeyModifier.WIN)
    wait(1)
    paste(unicode(i, "utf8"))
    print("ok")
"""


"""
a2 = "dir D:\\test /ad /b /s >del.txt"
a3 = "for /F %i in (del.txt) do rd %i /s /q"
a4 = 'PowerShell -Command "& {get-content del.txt -encoding default | set-content del_utf8.txt -encoding utf8}"'
os.system(a1)
os.system(a2)
os.system(a4)
# os.system(a3)

with open('del_utf8.txt', 'r') as f:
    qq = f.read()
    ss = qq.split("\n")
    e_list = []
    for i in ss:
        print(i)
        er = '\"' + i + '\"'
        print(er)
        e_list.append(er)
del e_list[-1]
print(e_list)  
print(len(e_list))

with open('del_utf8.txt', 'w') as f:
    for i in e_list:
        f.write(i)
        f.write('\n')

with open('del_utf8.txt', 'r') as f:
    qq = f.read()
    ss = qq.split("\n")

sq = random.sample(ss, 2)
for i in sq:
    type("r", KeyModifier.WIN)
    wait(1)
    paste(unicode(i, "utf8"))
    print("ok")
"""    

