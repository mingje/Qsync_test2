from sikuli import *
from library_qsync import *

def exist_check(file):
    cmd = "IF EXIST " + file + " (ECHO True) ELSE (ECHO False)"
    echo = os.popen(cmd).read()
    echo_result = echo.split("\n")
    return echo_result[0]

def copy_file(from_path, to_path, file):
    path_done = to_path + file
    copy_cmd = "XCOPY " + from_path + " " + to_path + " /I /E /Y"
    if exist_check(to_path) == "True" and exist_check(from_path) == "True":
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

def output_checksum_list(data_path):
    cmd = "D:\\fciv.exe -r " + data_path
    che_cmd = os.popen(cmd).read()
    output_line = che_cmd.split("\n")
    che_list = []
    start_flag = 0
    for i in output_line:
        # print(i,a.index(i))
        if "Start Time" in i:      
            add_flag = output_line.index(i)
            start_flag = 1
            print("start_flag:" + str(start_flag))
        elif "End Time" in i:
            break
        elif start_flag == 1 and output_line.index(i) > add_flag:
            if i != "":
                i = i.split(" ")
                che_list.append(i[0])
        else:
            pass
    return che_list

def output_checksum_file(data_path):
    check_list = output_checksum_list(data_path)
    week_info = week_current()
    checksum_file = "checksum_" + week_info + ".txt"
    with open(checksum_file, 'w') as e:
        for j in check_list:
            e.write(j)
            e.write('\n')

def output_checksum_list_from_file(checksum_path):
    checksum_path = to_path + file
    with open(checksum_path, 'r') as g:
        mark_data = g.read()
        mark_list = mark_data.split("\n")
        del mark_list[-1]
    return mark_list
"""
output_checksum_file("D:\\m")
week_info = week_current()
file = "checksum_" + week_info + ".txt"
from_path = os.getcwd() + "\\" + file
to_path = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\"
copy_file(from_path, to_path, file)
checksum_path = to_path + file
data_path = to_path + week_info
"""
def check_checksum(checksum_path, data_path):
    source_list = output_checksum_list_from_file(checksum_path)
    compare_list = output_checksum_list(data_path)
    if source_list == compare_list:
        flag = 1
        print("Checksum check PASS")
    else:
        flag = 0
        print("Checksum check FAIL")
    return flag
path_user = "user"
week_current = "Mon"
copy_path = "C:\\Users\\" + path_user + "\\@Qsync_test\\" + week_current
copy_path_cmd = "dir " + copy_path
print(copy_path_cmd)

#index = vowels.index('e')
#print('The index of e:', index)