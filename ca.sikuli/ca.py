from sikuli import *
from library_qsync import *



"""
path = "C:\\Users\\User\\@Qsync_test\\"
path_q = path + ".qsync"
attrib_cmd = "attrib -s -h -r " + path + "\\*.* && del " + path + "\\*.* /q"
dir_cmd = "dir " + path + " /ad /b /s >del.txt"
to_utf8 = 'PowerShell -Command "& {get-content del.txt -encoding default | set-content del_utf8.txt -encoding utf8}"'
os.system(attrib_cmd)
os.system(dir_cmd)
os.system(to_utf8)
# add mark to list
with open('del_utf8.txt', 'r') as f:
    path_list = f.read()
    path_list = path_list[3:]
    path_list_space = path_list.split("\n")
    print(path_list_space)
    switch_list = []
    for i in path_list_space:
        print(i)
        if i == path_q:
            pass
        else:
            mark_string = '\"' + i + '\"'
            print(mark_string)
            switch_list.append(mark_string)
print(len(switch_list))
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
    del mark_list[-1]
print(mark_list)
print(len(mark_list))
"""


"""
target = AT_PC_t1  
path1 = "C:\\team_folder_data"
path2 = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + target["folder_name"] + "\\"
copy_data(path1, path2, "by_week")
"""
"""
# delete_folder("D:\\test\\")

def delete_folder(path):
    cmd = "D:\\Qsync_test_stage2\\delete.bat " + path
    print(cmd)
    os.system(cmd)
    if current_data_counter(path = path , con_type = "folders") == 0:
        print("clean success")
    else:
        print("clean failed")
delete_folder("D:\\test\\")
path = "D:\\test\\"
print(current_data_counter(path = path , con_type = "folders"))
#delete_folder("D:\\test")
"""
def target_client():
    current_pc = get_pc_info("pc_name")
    for i in AT_list:
        if i["pc_name"] == current_pc:
            target_client = i
            break
        else:
            target_client = "unknown"
    return target_client


def run_path():
    source_path =sys.path[0]
    path_spl = source_path.split("\\")
    del path_spl[-1]
    out_path = "\\".join(path_spl)
    return out_path

def delete_folder(path):
    cmd = run_path() + "\\delete.bat " + path
    print(cmd)
    os.system(cmd)
    if current_data_counter(path = path , con_type = "folders") == 0:
        print("clean success")
    else:
        print("clean failed")

delete_folder(path="D:\\test\\")