from sikuli import *
from library_qsync import *

def exist_check(file):
    cmd = "IF EXIST " + file + " (ECHO True) ELSE (ECHO False)"
    echo = os.popen(cmd).read()
    e = echo.split("\n")
    return e[0]

path_from = "C:\\sikuli\\checksum.txt"
path_to = "D:\\m"
path_done = path_to + "\\checksum.txt"
copy_cmd = "XCOPY " + path_from + " " + path_to + "\ /I /E /Y"
if exist_check(path_to) == "True" and exist_check(path_from) == "True":
    exist_flag = 1
    os.system(copy_cmd)
    if exist_check(path_done) == "True":
        flag = 1
        print("Copy data success")
    else:
        flag = 0
    assert flag == 1, "Copy data failed"
else:
    exist_flag = 0
    print("Folder not existed")
assert exist_flag == 1, "Source or destination not exist"
"""
print(os.getcwd())
a = os.getcwd() + "\\" + "che.txt"
print(a)
"""
"""
cmd = "D:\\fciv.exe -r D:\\m1"
oo_cmd = os.popen(cmd).read()
#print(oo_cmd)
a = oo_cmd.split("\n")
print(a)
che_list = []
start_flag = 0
for i in a:
    # print(i,a.index(i))
    if "Start Time" in i:      
        add_flag = a.index(i)
        start_flag = 1
        print("start_flag:" + str(start_flag))
    elif "End Time" in i:
        break
    elif start_flag == 1 and a.index(i) > add_flag:
        if i != "":
            i = i.split(" ")
            che_list.append(i[0])
    else:
        print("pass")
print(che_list)
with open('checksum.txt', 'w') as e:
    for j in che_list:
        e.write(j)
        e.write('\n')
with open('checksum.txt', 'r') as g:
    mark_data = g.read()
    mark_list = mark_data.split("\n")
    del mark_list[-1]
print(mark_list)

if che_list == mark_list:
    print("f")
else:
    print("n")
"""


#index = vowels.index('e')
#print('The index of e:', index)