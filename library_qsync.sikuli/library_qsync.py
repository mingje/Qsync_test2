# -*- coding:utf-8 -*-
from sikuli import *
import os
import sys
import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

################# Testing Info ###################
AT_VM_S2 = {
    "ip": "10.20.241.134",
    "folder_name": "share_test_desktop-kp8ovfb",
    "pc_name": "desktop-kp8ovfb",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_PC_S1 = {
    "ip": "10.20.241.131",
    "folder_name": "share_test_desktop-11ih26e",
    "pc_name": "desktop-11ih26e",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_PC_S2 = {
    "ip": "10.20.241.132",
    "folder_name": "share_test_desktop-u1af6o9",
    "pc_name": "desktop-u1af6o9",
    "ac": "Utility_test",
    "pwd": "swqa"
        }
AT_PC_S3 = {
    "ip": "10.20.241.138",
    "folder_name": "share_test_erincheng-pc",
    "pc_name": "erincheng-pc",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_VM_S3 = {
    "ip": "10.20.241.133",
    "folder_name": "share_test_dqv-pc1",
    "pc_name": "dqv-pc1",
    "ac": "dqv1",
    "pwd": "swqa"
        }
AT_VM_S1 = {
    "ip": "10.20.241.135",
    "folder_name": "share_test_desktop-d3ogd7m",
    "pc_name": "desktop-d3ogd7m",
    "ac": "dqv",
    "pwd": "swqa"
        }
AT_list = [AT_VM_S1, AT_VM_S2, AT_VM_S3, AT_PC_S2]

Mon = {
    "mark": "Mon",
    "share_file": 124,
    "share_folder": 11,
    "share_size": 11362,
    "team_file": 3,
    "team_folder": 8,
    "team_size": 44
        }
Tue = {
    "mark": "Tue",
    "share_file": 2,
    "share_folder": 4,
    "share_size": 332568,
    "team_file": 3,
    "team_folder": 5,
    "team_size": 2345
        }
Wed = {
    "mark": "Wed",   
    "share_file": 2,
    "share_folder": 4,
    "share_size": 332568,
    "team_file": 3,
    "team_folder": 5,
    "team_size": 2345
        }
Thu = {
    "mark": "Thu", 
    "share_file": 2,
    "share_folder": 4,
    "share_size": 332568,
    "team_file": 3,
    "team_folder": 5,
    "team_size": 2345
        }
Fri = {
    "mark": "Fri",
    "share_file": 4,
    "share_folder": 4,
    "share_size": 332568,
    "team_file": 3,
    "team_folder": 5,
    "team_size": 2345
        }
Sat = {
    "mark": "Sat",
    "share_file": 0,
    "share_folder": 2,
    "share_size": 0,
    "team_file": 0,
    "team_folder": 2,
    "team_size": 0
        }
Sun =  {
    "mark": "Sun",
    "share_file": 0,
    "share_folder": 2,
    "share_size": 0,
    "team_file": 0,
    "team_folder": 2,
    "team_size": 0
        }
week_list = [Mon, Tue, Wed, Thu, Fri, Sat, Sun]

sys_path = sys.path[0]
sys_path_split = sys_path.split("\\")
del sys_path_split[-1]
print(sys_path_split)
delimiter = "\\"
picture_path = delimiter.join(sys_path_split) + "\\screenshot\\"
print(picture_path)

def nas_detail(**kwargs):
    nas = {}   
    nas["lanip"] = kwargs.get("lanip")   
    nas["ac"] = kwargs.get("ac")
    nas["pwd"] = kwargs.get("pwd")
    return nas

def search_path(picture_name):
    check_path = picture_path + picture_name + "\\"
    print(check_path)
    search_list = os.listdir(check_path)
    print(search_list)
    for i in search_list:
        print(i)
        final_path = check_path + i
        print(final_path) 
        if exists(final_path):
            print("Found picture")
            flag = final_path
            break
        else:
            print("Not Found picture")
            flag = final_path
    return flag

def target_week():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    now_week = week_current()
    print(now_week)
    for i in week_list:
        if i["mark"] == now_week:
            return i
            break
        else:
            pass


################# System related function ###################
def get_os_bit():
    os_bit = os.popen("echo %PROCESSOR_ARCHITECTURE%").read()
    if "64" in os_bit: 
        os_bit = "64" 
    else:
        os_bit = "32"
    return os_bit

# get_pc_info(info_name = "pc_name" or "user_name")
def get_pc_info(info_name):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    info_name_list = []
    pc_info = os.popen("whoami").read()
    pc_info_list = pc_info.split("\\")
    pc_name = pc_info_list[0]
    user_name = pc_info_list[1]
    user_name = user_name[0:-1]
    if info_name == "pc_name":
        return pc_name
    else:
        return user_name

def get_os_ver():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    os_dir = os.popen("ver").read()
    os_split = os_dir.split("[")
    os_split1 = os_split[1].split(" ")
    os_split2 = os_split1[1].split(".")
    if os_split2[0] == "10":
        print("OS is Win10")
        return "Win10"
    elif os_split2[0] == "6":
        print("OS is Win7")
        return "Win7"
    else:
        print("Unknown OS")
        return "Unknown OS"

def week_current():
    localtime = time.asctime( time.localtime(time.time()) )
    print "Locatime:", localtime
    localtime_space = localtime.split(" ")
    week_current = localtime_space[0]
    return week_current

def mount_disk(ip, folder_name, username, password, disk):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    mount_cmd = "net use " + disk + ": " + "\\\\" + ip + "\\" + folder_name + " /user:" + username + " " + password
    print(mount_cmd)
    os.system(mount_cmd)
    dir_cmd = "dir " + disk + ":\\"
    flag = os.system(dir_cmd)
    if flag == 0:
        print("Mount success")
    else:
        print("Mount failed")
    # assert flag == 0, "Mount failed"
    wait(1)

def unmount_disk(disk):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    os.system("net use * /d /YES")
    dir_cmd = "dir " + disk + ":\\"
    flag = os.system(dir_cmd)
    if flag == 1:
        print("Unmount success")
    else:
        pass
    assert flag == 1, "Unmount failed"
    wait(1)

# clean_remote_disk("w")
def clean_remote_disk(disk):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    clean_cmd = "rd /s/q " + disk + ":\\"
    try:
        os.system(clean_cmd)
    except:
        pass
    path = disk + ":\\"
    if counter_data("icon_total", "single", path) == 0:
        print("clean success")
    else:
        print("clean failed")

def run_path():
    source_path =sys.path[0]
    path_spl = source_path.split("\\")
    del path_spl[-1]
    out_path = "\\".join(path_spl)
    return out_path

# delete_folder("D:\\test\\")
def delete_folder(path):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    cmd = run_path() + "\\delete.bat " + path
    print(cmd)
    os.system(cmd)
    if counter_data("icon_total", "single", path) == 0:
        print("Clean success")
    else:
        print("Clean failed")

def send_mail(test_pc):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    gmail_user = 'stevenhsu@qnap.com'
    gmail_password = 'Qwer!23456' # your gmail password
    gmail_to = ['mingje1104@gmail.com', 'danielhuang@qnap.com', 'rexhchsu@qnap.com']
    gmail_cc = ['stevenhsu@qnap.com']
    COMMASPACE = ', '
    #msg = MIMEText('content')
    msg = MIMEMultipart()
    msg['Subject'] = 'ERROR'
    msg['From'] = "AT manager"
    msg['To'] = COMMASPACE.join(gmail_to)
    msg['cc'] = COMMASPACE.join(gmail_cc)
    part = MIMEText(test_pc + " error")
    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,gmail_to,msg.as_string())
    server.quit()
    print('Email sent!')

def wait_time(loop, waittime):
    x = 0
    for i in range(loop):
        if x == 0:
            print("start to wait")
        else:    
            pass
        wait(waittime)
        print("Pass " + str(waittime) + " secs")
        x = x + 1

    
################# Windows behavior function ###################
# open folder with win browser (open_folder("D:\\test"))
def open_folder(folder_path):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    wait(2)
    for j in range(3):
        wait(2)
        type("r", KeyModifier.WIN)
        wait(2)
        if folder_path == "default":
            path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\"
        else:
            path = folder_path
        print(path)
        paste(unicode(path, "utf8"))
        print("paste path")
        wait(1)
        type(Key.TAB)
        wait(3)
        if exists(Pattern(search_path("confirm_button")).similar(0.70)):
            break
        else:
            print("paste fail, redo")
            type(Key.F4, KeyModifier.ALT)
        
    # type(path)
    type(Key.ENTER)
    wait(3)
    type(Key.UP, KeyModifier.WIN)

def open_folder_cmd(folder_path, os_ver):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    for i in range(3):
        wait(2)
        if folder_path == "default":
            path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\"
        else:
            path = folder_path
        print(path)
        cmd = "explorer " + path
        os.system(cmd)  
        wait(3)
        if check_open_folder(os_ver) == 1:
            print("Open folder success")
            break
        else:
            print("Open folder fail")
    if check_max_window(os_ver) == 1:
        print("Max window success")
    else:
        print("Max windows fail")
    wait(1)

def set_browser_sty(os_ver):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    if os_ver == "Win10":

        check_region = Region(59,7,273,44)
        
        check_region.click(Pattern(search_path("view_tab")).similar(0.70))
        wait(5)
        click(Pattern(search_path("big_view_button")).similar(0.70))
        wait(5)
        click(Pattern(search_path("browser_window_button")).similar(0.70))
        wait(2)
        if exists(Pattern(search_path("show_browser_window")).similar(0.90)):
            print("browser window opened status")
            click(Pattern(search_path("show_browser_window")).similar(0.90))
        elif exists(Pattern(search_path("hide_browser_window")).similar(0.90)):
            print("browser window closed status")
            type(Key.ENTER)
        else:
            print("set browser failed")
        wait(1)
        type(Key.F5)
        wait(1)
    elif os_ver == "Win7":
        type("v", KeyModifier.ALT)
        wait(2)
        type("r", KeyModifier.SHIFT)
        wait(2)
        type(Key.ENTER)
        wait(2)
        click(Pattern(search_path("manager_button")).similar(0.70))
        wait(3)
        click(Pattern(search_path("configuration_button")).similar(0.70))
        wait(3)
        if exists(Pattern(search_path("show_browser_window_7")).similar(0.90)):
            print("browser window opened status")
            click(Pattern(search_path("show_browser_window_7")).similar(0.90))
        elif exists(Pattern(search_path("hide_browser_window_7")).similar(0.90)):
            print("browser window closed status")
            type(Key.ENTER)
        else:
            print("set browser failed")
        wait(1)
        type(Key.F5)
        wait(1)
    else:
        print("Failed")

def check_open_folder(os_ver):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    print("***Start to check_open_folder***")
    if os_ver == "Win10":
        if exists(Pattern(search_path("refresh_button")).similar(0.70)):
            click(Pattern(search_path("refresh_button")).similar(0.70))
            flag = 1
        else:
            flag = 0
    else:
        if exists(Pattern(search_path("refresh_button_7")).similar(0.70)):
            click(Pattern(search_path("refresh_button_7")).similar(0.70))
            flag = 1
        else:
            flag = 0
    return flag 

def check_max_window(os_ver):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    flag = 0
    for i in range(3):
        if os_ver == "Win10":
            click(Pattern(search_path("refresh_button")).similar(0.70))
        else:
            click(Pattern(search_path("refresh_button_7")).similar(0.70))
        type(Key.UP, KeyModifier.WIN)
        wait(3)
        if exists(Pattern(search_path("maxwindow_folder_icon")).similar(0.70)):
            print("Max window")
            flag = 1
            break
        else:
            print("Not max window")
            flag = 0
    return flag


################# Qsync opration function ###################
def open_qsync(os_bit):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    flag = 0
    for i in range(3):
        if os_bit == "64": 
            qsync = "C:\Program Files (x86)\QNAP\Qsync\Qsync.exe"
        else:
            qsync = "C:\Program Files\QNAP\Qsync\Qsync.exe"
        openApp(qsync)
        wait(5)
        if exists(Pattern(search_path("delete_button")).similar(0.70)):
            click(Pattern(search_path("delete_button")).similar(0.70))
        else:
            print("No warning")
        if os_bit == "64": 
            os.system('"C:\\Program Files (x86)\\QNAP\\Qsync\\Qsync.exe"')
        else:
            os.system('"C:\\Program Files\\QNAP\\Qsync\\Qsync.exe"')
        wait(5)
        if exists(Pattern(search_path("minwindow_icon")).similar(0.80)):
            click(Pattern(search_path("minwindow_icon")).similar(0.80))
        elif exists(Pattern(search_path("maxwindow_icon")).similar(0.70)):
            print("Max Qsync window")
        else:
            print("Max Qsync window failed")
        wait(5)
        if exists(Pattern(search_path("qsync_logo")).similar(0.70)):
            print("Open Qsync success")
            flag = 1
            break
        else:
            flag = 0
    assert flag == 1, "Open Qsync failed"

def close_qsync():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    os.system("taskkill /f /im Qsync.exe")
    wait(3)
    if check_qsync_live() == False:
        flag = 1
        print("Close Qsync success")
    else:
        flag = 0
    assert flag == 1, "Close Qsync failed"
    if exists(Pattern(search_path("qsync_logo")).similar(0.70)):
        print("Close Qsync fail_UI")
    else:
        print("Close Qsync success_UI")

def remove_nas_profile():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    click(Pattern(search_path("more_button")).similar(0.70))
    wait(2)
    click(Pattern(search_path("removeNAS_option")).similar(0.70))
    wait(2)
    click(Pattern(search_path("option_button")).similar(0.70))
    wait(1)
    type(Key.DOWN)
    wait(1)
    type(Key.ENTER)
    wait(5)
    waitVanish((Pattern(search_path("pleasewait_string")).similar(0.70)),600)
    if exists(Pattern(search_path("host_field")).similar(0.70)):
        print("Remove NAS success")
        flag = 1
    else:
        flag = 0
    assert flag == 1, "Remove NAS failed"

def login_pair(ip, ac, pwd):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    click(Pattern(search_path("host_field")).similar(0.70))
    wait(1)
    type(ip)
    wait(1)
    type(Key.TAB)
    type(ac)
    wait(1)
    type(Key.TAB)
    type(pwd)
    wait(1)
    type(Key.ENTER)
    waitVanish((Pattern(search_path("pairing_string")).similar(0.70)),120)
    if exists(Pattern(search_path("pairing_string")).similar(0.70)):
        print("over 2 mins..")
    elif exists(Pattern(search_path("loginfail_string")).similar(0.70)):
        print("login failed")
    elif exists(Pattern(search_path("qsyncpath_string")).similar(0.70)):
        print("login success")
    else:
        print("unknown status")
    wait(5)
    click(Pattern(search_path("addfolder_icon")).similar(0.70))
    wait(2)
    rregion = Region(447,151,387,368)
    if rregion.exists(Pattern(search_path("browsefolder_string")).similar(0.70)):
        print("open")
    else:
        print("open Failed")
    type("M")
    wait(1)
    type("@Qsync_test")
    wait(1)
    type(Key.ENTER)
    wait(3)
    if exists(Pattern(search_path("folder_exist_icon")).similar(0.70)):
        type(Key.ENTER)
        wait(2)
    else:
        pass
    type(Key.ENTER)
    wait(1)
    click(Pattern(search_path("finish_button")).similar(0.70))

def check_qsync_live():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    cmd = 'TASKLIST /FI "imagename eq Qsync.exe" /svc'
    tasklist_cmd = os.popen(cmd).read()
    if "Qsync" in tasklist_cmd:
        return True
    else:
        return False

def close_qsync_UI():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    wait(1)
    click(Pattern(search_path("close_button")).similar(0.70))
    wait(2)
    if exists(Pattern(search_path("qsync_logo")).similar(0.70)):
        flag = 0
    else:
        print("Close Qsync UI success")
        flag = 1
    assert flag == 1, "Close Qsync UI fail"
    wait(1)

################# Data sync function ###################
# input path then get check list (get_check_icon_list(path = "D:\\test"))
def get_check_icon_list(path, os_ver):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    path = path
    path_q = path + "\\.qsync"
    attrib_cmd = "attrib -s -h -r " + path + "\\*.* && del " + path + "\\*.* /q"
    dir_cmd = "dir " + path + " /ad /b /s >del.txt"
    if os_ver == "Win10":
        to_utf8 = 'PowerShell -Command "& {get-content del.txt -encoding default | set-content del_utf8.txt -encoding utf8}"'
    elif os_ver == "Win7":
        to_utf8 = 'PowerShell -Command "& {get-content del.txt -encoding String | set-content del_utf8.txt -encoding utf8}"'
    else:
        print("Unknown OS")
    os.system(attrib_cmd)
    os.system(dir_cmd)
    print(to_utf8)
    wait(10)
    os.system(to_utf8)
    # add mark to list
    with open('del_utf8.txt', 'r') as f:
        path_list = f.read()
        path_list = path_list[3:]
        path_list_space = path_list.split("\n")
        switch_list = []
        for i in path_list_space:
            if i == path_q:
                pass
            else:
                mark_string = '\"' + i + '\"'
                switch_list.append(mark_string)
    del switch_list[-1]
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
    return mark_list

def check_icon_no(data_items, row_items):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    """
    data_items = 110
    row_items = 11
    """
    # get items at first page
    try:
        a = findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
        b = []
        for i in a:
            b.append(i)
        print("First page catch:" + str(len(b)))
    except:
        b = []
    page_item_no = len(b)
    d = []
    if page_item_no == 0:
        print("number: " + str(len(b)))
    elif data_items <= page_item_no:
        print("number: " + str(len(b)))
    else:
        click_region = Region(1194,583,86,137)
        for i in range(5):
            if click_region.exists(Pattern(search_path("down_button")).similar(0.70)):
                click_region.click(Pattern(search_path("down_button")).similar(0.70))
                wait(1)
                xregion = Region(13,562,1239,84)
                c = xregion.findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
                for j in c:
                    d.append(j)
                print(len(d))
                if exists(Pattern(search_path("down_end_button")).similar(0.70)):
                    print("move to end")
                    break
                else:
                    pass
            else:
                print("number: " + str(len(b)))
                break
    ss = len(b) + len(d)
    if len(b) > data_items:
        print(ss)
    elif ss > data_items:
        ss = ss -row_items
        print(ss)
    else:
        print(ss)
    return ss   
              
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
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    if counter_type == "single":
        dir_cmd = "dir " + path
    elif counter_type == "all":
        dir_cmd = "dir " + path + " /s"
    else:
        print("Unknown counter_type")
    dir_result = os.popen(dir_cmd).read()
    # print(dir_result)
    dir_result_line = dir_result.split("\n")
    if data_type == "file":
        try:
            file_no = int(output_counter_list("file", dir_result_line)[0])
        except:
            file_no = -1
        return file_no
    elif data_type == "folder":
        try:
            folder_no = int(output_counter_list("folder", dir_result_line)[0])
        except:
            folder_no = -1
        return folder_no
    elif data_type == "size":
        try:
            file_size = output_counter_list("file", dir_result_line)[2]
            file_size_f = size_to_int(file_size)
        except:
            file_size_f = -1
        return file_size_f
    elif data_type == "total":
        try:
            file_no = int(output_counter_list("file", dir_result_line)[0])
            folder_no = int(output_counter_list("folder", dir_result_line)[0])
            total = folder_no + file_no
        except:
            total = -1
        return total
    elif data_type == "icon_total":
        try:
            file_no = int(output_counter_list("file", dir_result_line)[0])
            folder_no = int(output_counter_list("folder", dir_result_line)[0])
            icon_total = folder_no + file_no -2
        except:
            icon_total = -1
        return icon_total
    else:
        return 0

def counter_surplus_no(data_type, counter_type, path):
    try:
        surplus_no = counter_data(data_type, counter_type, path)
        if surplus_no == -1:
            surplus_no = 0
        else:
            surplus_no = surplus_no
    except:
        surplus_no = 0
    return surplus_no

def size_to_int(size):
    size = size.replace(',', '')
    return int(size)

def check_data_result(path1, path2):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    right_week = target_week()
    if path1 == "fixed_path_share": 
        path_from_total = right_week["share_file"] + right_week["share_folder"]
        path_from_size = right_week["share_size"]
    elif path1 == "fixed_path_team":
        path_from_total = right_week["team_file"] + right_week["team_folder"]
        path_from_size = right_week["team_size"]
    else:
        path_surplus = path1 + "\\.qsync" 
        path_from_total = counter_data("total", "all", path1) - counter_surplus_no("total", "all", path_surplus)
        path_from_size = counter_data("size", "all", path1)- counter_surplus_no("size", "all", path_surplus)
    print("Source total = " + str(path_from_total))
    print("Source size = " + str(path_from_size))  
    
    path_surplus = path2 + "\\.qsync" 
    path_to_total = counter_data("total", "all", path2) - counter_surplus_no("total", "all", path_surplus)
    print("Destination total = " + str(path_to_total))
    path_to_size = counter_data("size", "all", path2) - counter_surplus_no("size", "all", path_surplus)
    print("Destination size = " + str(path_to_size))

    if path_from_total == path_to_total and path_from_size == path_to_size:
        print("Copy data consistent")
        return True
    else:
        print("Copy data inconsistent")
        return False

# copy_data("D:\\test", "D:\\test2\\", "by_week")
def copy_data(path1, path2, check_type):   
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
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

def outut_page_items():
    current_icon_list = []
    try:
        icon_findall = findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
        for i in icon_findall:
            current_icon_list.append(i)
    except:
        current_icon_list = []
    print("current page icon: " + str(len(current_icon_list)))
    return len(current_icon_list)

def output_line_items(): 
    line_list = []
    try:
        xregion = Region(7,526,1247,127)
        icon_findline = xregion.findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
        for j in icon_findline:
            line_list.append(j)
    except:
        line_list = []
    print("current line icon: " + str(len(line_list)))
    return(len(line_list))

def check_icon_result(data_items, row_items, page_item_no):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    if data_items == page_item_no:
        print("Icon check PASS: " + str(page_item_no))
        flag = 1
    elif data_items < page_item_no: 
        print("Icon check fail")
        flag = 2
    else:
        if page_item_no % row_items == 0 and data_items > row_items * 3:
            flag = 0
        else:
            print("Icon check fail")
            flag = 3
    return flag

def down_icon_check(data_items, row_items ,page_item_no):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    quotient = data_items / row_items
    remainder = data_items % row_items
    exclude_no = page_item_no / row_items
    if remainder == 0:
        down_time = quotient - exclude_no + 1
    else:
        down_time = quotient - exclude_no + 2
    print("Max down times is: " + str(down_time))
    result_icon = 0
    for i in range(down_time):
        # click_region = Region(1253,625,27,36)
        try:
            click(Pattern(search_path("down_button")).similar(0.70))
        except:
            print("Press down button fail")
        add_item_no = output_line_items()
        result_icon = result_icon + add_item_no
        if add_item_no != row_items:
            break
        else:
            print(result_icon)
    total_no = page_item_no + result_icon
    if total_no > data_items:
        total_final = total_no -11
    else:
        total_final = total_no
    print("first" + str(page_item_no))
    print("add items: " + str(result_icon))
    print("Total number: " + str(total_no))
    print("Final total number: " + str(total_final))
    return total_final

def check_icon_no_N(data_items, row_items):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    # get items at first page
    x = 0
    flag = 0
    for i in range(2):
        if x == 0:
            first_page_item_no = outut_page_items()
            page_item_no = first_page_item_no
            print("First page icon no= " + str(first_page_item_no))
        else:
            page_item_no = down_icon_check(data_items, row_items, first_page_item_no)
        icon_result = check_icon_result(data_items, row_items , page_item_no)
        if icon_result == 1:
            print("End icon check: Result PASS")
            flag = 1
            break
        elif icon_result == 0:
            print("Enter advanced check step")
            flag = 0
        else:
            print("End icon check: Result FAIL")
            flag = 0
            break
        x = x + 1
    return flag

def check_sync_icon(path, os_ver, os_bit):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    print(path)
    if counter_data("icon_total", "single", path) != -1:
        open_folder_cmd(path, os_ver)
        set_browser_sty(os_ver)
        data_items = counter_data("icon_total", "single", path)
        print("Check items = " + str(data_items))
        if os_bit == "64":
            row_items = 11
        else:
            row_items = 17
        if check_icon_no_N(data_items, row_items) == 1:
            print("pass icon check")
            flag = 1
        else:
            print("fail icon check")
            flag = 0
        if os_ver == "Win10":
            click(Pattern(search_path("refresh_button")).similar(0.70))
        else:
            click(Pattern(search_path("refresh_button_7")).similar(0.70))    
        type(Key.F4, KeyModifier.ALT)
    else:
        print("pass icon check, no folder")
        flag = 1
    return flag

def random_icon_check(ran_switch, ran_no, os_ver, os_bit, *args):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    if isinstance(args[0], list) == True:
        args = args[0]
    else:
        args = args
    # decide run_list
    if ran_switch == "Y":
        if len(args) == 1:
            run_list = random.sample(args, 1)
        else:
            run_list = random.sample(args, ran_no)
    else:
        run_list = args 
        ran_no = 1
    for i in run_list:
        print(i)
        flag = check_sync_icon(i, os_ver, os_bit)
        if flag != 1:
            break
    return flag

def check_team_folder(os_ver, os_bit):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    week_info = week_current()
    qa = get_pc_info("pc_name")
    for i in AT_list:
        ew = i["folder_name"].split("_")
        if week_info == "Sat" or week_info == "Sun":
            path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + i["folder_name"]
        else:
            path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + i["folder_name"] + "\\" + week_info
        if ew[-1] == qa:
            pass
        else:
            # mount_disk(i["ip"],i["folder_name"],i["ac"],i["pwd"],"w") 
            check_data_result("fixed_path_team", path)
            check_sync_icon(path = path, os_ver = os_ver, os_bit = os_bit)
            adv_flag = counter_data("icon_total", "single", path)
            if adv_flag == 0:
                print("Pass advanced icon check")
            elif adv_flag == -1:
                print("Pass advanced icon check, no folder")
            else:   
                mark_list = get_check_icon_list(path, os_ver)
                random_icon_check("Y", 2, os_ver, os_bit, mark_list)
            # unmount_disk("w")
            
def check_share_folder(os_ver, os_bit):
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    i = AT_PC_S1
    week_info = week_current()
    if week_info == "Sat" or week_info == "Sun":
        path = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\"
    else:
        path = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\" + week_info 
    print(path)
    # mount_disk(i["ip"],"@Qsync_test",i["ac"],i["pwd"],"w") 
    check_data_result("fixed_path_share", path)
    check_sync_icon(path = path, os_ver = os_ver, os_bit = os_bit)
    adv_flag = counter_data("icon_total", "single", path)
    if adv_flag == 0:
        print("Pass advanced icon check")
    elif adv_flag == -1:
        print("Pass advanced icon check, no folder")
    else:   
        mark_list = get_check_icon_list(path, os_ver)
        random_icon_check("Y", 2, os_ver, os_bit, mark_list)
    # unmount_disk("w")

def check_main_sync():
    fun_name = sys._getframe().f_code.co_name
    print("***Start to " + fun_name + " ***")
    flag = 0
    for i in range(10):
        wait(4)
        if exists(Pattern(search_path("syncdone_icon")).similar(0.70)):
            print("Sync success, start to check data")
            flag = 1
        elif exists(Pattern(search_path("syncing_icon")).similar(0.70)):
            print("Syncing...")
            flag = 2
        else:
            print("Sync failed")
            flag = 0
    return flag

def target_client():
    current_pc = get_pc_info("pc_name")
    print(current_pc)
    for i in AT_list:
        if i["pc_name"] == current_pc:
            target_client = i
            break
        else:
            target_client = "unknown"
    return target_client

path1 = "D:\\test"
path_surplus = path1 + "\\.qsync"
print(counter_surplus_no("total", "all", path_surplus))