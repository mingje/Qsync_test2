from sikuli import *
from library_qsync import *

def exist_check(file):
    cmd = "IF EXIST " + file + " (ECHO True) ELSE (ECHO False)"
    echo = os.popen(cmd).read()
    echo_result = echo.split("\n")
    return echo_result[0]

def copy_file(from_path, to_path, file):
    path_done = to_path + file
    copy_cmd = "COPY " + from_path + " " + to_path + " /Y"
    print(copy_cmd)
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
    week_info = week_current()
    file = "checksum_" + week_info + ".txt"
    checksum_path = checksum_path + file
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

def check_checksum_share():
    week_info = week_current()
    if week_info == "Sat" or week_info == "Sun":
        print("Skip Checksum_share")
        check_flag = 1
    else:
        checksum_path = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\"  
        print(checksum_path)
        data_path = checksum_path + week_info
        if check_checksum(checksum_path, data_path) == 1:
            print("Checksum_share match")
            check_flag = 1
        else:
            print("Checksum_share not match")
            check_flag = 0
    return check_flag

def check_checksum_team():
    week_info = "Sun"
    qa = get_pc_info("pc_name")
    check_flag = 0
    for i in AT_list:
        ew = i["folder_name"].split("_")
        if week_info == "Sat" or week_info == "Sun":
            print("Skip Checksum_share: " + i["folder_name"])
            check_flag = 1
            break
        else:
            checksum_path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + i["folder_name"] + "\\"
            data_path = checksum_path + week_info
        if ew[-1] == qa:
            pass
        else:
            if check_checksum(checksum_path, data_path) == 1:
                print("Checksum_team PASS: " + i["folder_name"])
                check_flag = 1
            else:
                print("Checksum_team FAIL: " + i["folder_name"])
                check_flag = 0
                break
    return check_flag
AT_VM_S2 = {
    "ip": "10.20.241.135",
    "folder_name": "share_test_dqv-pc1",
    "pc_name": "dqv-pc1",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_PC_S2 = {
    "ip": "10.20.241.135",
    "folder_name": "share_test_desktop-u1af6o9",
    "pc_name": "desktop-u1af6o9",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_list = [AT_VM_S2, AT_PC_S2]

error_code = "\n0: check main sync UI Fail \n1: Checksum check FAIL \n" + "2: Data files, folders and size not match \n" \
        + "3: Root folder icon check FAIL \n4: Advanced folder icon check FAIL"
print(error_code)
#index = vowels.index('e')
#print('The index of e:', index)