from sikuli import *
from library_qsync import *

# counter_data
# counter_type = file or folder; result_line = dir_result_line
def output_counter_list(out_type, result_line):
    if out_type == "folder":
        data_space = result_line[-2].split(" ")
    elif out_type == "file":
        data_space = result_line[-3].split(" ")
    else:
        print("gg")
    no_list = []
    for i in data_space:
        if i != "":
            no_list.append(i)
    return no_list

# data_type = file, folder, size, total(file+folde),icon_total(file+folder-2), counter_type = single or all
# icon_total + single = icon check no
# current_data_counter
def counter_data(data_type, counter_type, path):
    if counter_type == "single":
        dir_cmd = "dir " + path
    elif counter_type == "all":
        dir_cmd = "dir " + path + " /s"
    else:
        print("Unknown counter_type")
    dir_result = os.popen(dir_cmd).read()
    print(dir_result)
    dir_result_line = dir_result.split("\n")
    if data_type == "file":
        file_no = int(output_counter_list("file", dir_result_line)[0])
        return file_no
    elif data_type == "folder":
        folder_no = int(output_counter_list("folder", dir_result_line)[0])
        return folder_no
    elif data_type == "size":
        file_size = output_counter_list("file", dir_result_line)[2]
        return file_size
    elif data_type == "total":
        file_no = int(output_counter_list("file", dir_result_line)[0])
        folder_no = int(output_counter_list("folder", dir_result_line)[0])
        total = folder_no + file_no
        return total
    elif data_type == "icon_total":
        file_no = int(output_counter_list("file", dir_result_line)[0])
        folder_no = int(output_counter_list("folder", dir_result_line)[0])
        icon_total = folder_no + file_no -2
        return icon_total
    else:
        return 0

counter_data("folder", "all", "D:\\test")
# data_type, counter_type, path
# check size & total
def check_data_result(path1, path2):
    path_from_total = counter_data("total", "all", path1)
    print("Source total = " + str(path_from_total))
    path_from_size = counter_data("size", "all", path1)
    print("Source size = " + path_from_size)
    path_to_total = counter_data("total", "all", path2)
    print("Destination total = " + str(path_to_total))
    path_to_size = counter_data("size", "all", path2)
    print("Destination size = " + path_to_size)
    if path_from_total == path_to_total and path_from_size == path_to_size:
        print("Copy data consistent")
        return True
    else:
        print("Copy data inconsistent")
        return False

# copy_data("D:\\test", "D:\\test2\\", "by_week")
def copy_data(path1, path2, check_type):   
    path_from = path1
    if check_type == "by_week":
        path_to = path2 + week_current()
    else:
        path_to = path2
    dir_cmd = "dir " + path2
    print(dir_cmd)
    copy_cmd = "XCOPY " + path_from + " " + path_to + "\ /I /E"
    if os.system(dir_cmd) == 0:
        os.system(copy_cmd)
        if check_data_result(path1 = path_from, path2 = path_to) == 1:
            print("Copy data success")
        else:
            print("Copy data failed")
    else:
        print("Folder not existed")
        
def check_sync_icon(path):
    print(path)
    open_folder_cmd(path)
    set_browser_sty()
    data_items = counter_data("icon_total", "single", path)
    print("Check items = " + str(data_items))
    row_items = 11
    if data_items == check_icon_no(data_items, row_items):
        print("pass icon check")
        flag = 1
    else:
        print("fail icon check")        
        flag = 0
    if get_os_ver() == "Win10":
        click(Pattern(search_path("refresh_button")).similar(0.70))
    else:
        click(Pattern(search_path("refresh_button_7")).similar(0.70))    
    type(Key.F4, KeyModifier.ALT)
    return flag





# old code
def counter_data(data_line, con_type):
    data_space = data_line.split(" ")
    no_list = []
    for i in data_space:
        if i != "":
           no_list.append(i)
    if con_type == "size":
        return no_list[2]
    else:
        return no_list[0]
# con_type = size, folders, total (current_data_counter("D:\\test","total"))
def current_data_counter(path, con_type):
    if con_type == "folders":
        dir_cmd = "dir " + path
    else:
        dir_cmd = "dir " + path + " /s"
    dir_result = os.popen(dir_cmd).read()
    dir_result_line = dir_result.split("\n")
    files_no = dir_result_line[-3]
    subfolders_no = dir_result_line[-2]
    total_data_no = int(counter_data(files_no, "amount")) + int(counter_data(subfolders_no, "amount"))
    current_data_no = total_data_no - 2
    current_data_size = counter_data(files_no, "size")
    current_data_size1 = current_data_size.split(',')
    if con_type == "size":
        return current_data_size1[0]
    elif con_type == "folders":
        return current_data_no
    else:
        return total_data_no

def check_copy_result(path1, path2):
    path_from_amount = current_data_counter(path1, con_type = "amount")
    print(path_from_amount)
    path_from_size = current_data_counter(path1, con_type = "size")
    print(path_from_size)
    path_to_amount = current_data_counter(path2, con_type = "amount")
    print(path_to_amount)
    path_to_size = current_data_counter(path2, con_type = "size")
    print(path_to_size)
    if path_from_amount == path_to_amount and path_from_size == path_to_size:
        print("Copy data consistent")
        return True
    else:
        print("Copy data inconsistent")
        return False

# copy_data("D:\\test", "D:\\test2\\", "by_week")
def copy_data(path1, path2, check_type):   
    path_from = path1
    if check_type == "by_week":
        path_to = path2 + week_current()
    else:
        path_to = path2
    dir_cmd = "dir " + path2
    print(dir_cmd)
    copy_cmd = "XCOPY " + path_from + " " + path_to + "\ /I /E"
    if os.system(dir_cmd) == 0:
        os.system(copy_cmd)
        if check_copy_result(path1 = path_from, path2 = path_to) == 1:
            print("Copy data success")
        else:
            print("Copy data failed")
    else:
        print("Folder not existed")
        
def check_sync_icon(path):
    print(path)
    open_folder_cmd(path)
    set_browser_sty()
    data_items = current_data_counter(path, "folders")
    print("data_items= " + str(data_items))
    row_items = 11
    if data_items == check_icon_no(data_items, row_items):
        print("pass icon check")
        flag = 1
    else:
        print("fail icon check")        
        flag = 0
    if get_os_ver() == "Win10":
        click(Pattern(search_path("refresh_button")).similar(0.70))
    else:
        click(Pattern(search_path("refresh_button_7")).similar(0.70))    
    type(Key.F4, KeyModifier.ALT)
    return flag
