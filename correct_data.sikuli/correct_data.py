from sikuli import *
from library_qsync import *
"""
Mon = {
    "mark": "Mon",
    "file": 2,
    "folder": 4,
    "size": 332568,
        }
Tue = {
    "mark": "Tue",
    "file": 2,
    "folder": 4,
    "size": 332568,
        }
Wed = {
    "mark": "Wed",   
    "file": 2,
    "folder": 4,
    "size": 332568,
        }
Thu = {
    "mark": "Thu", 
    "file": 2,
    "folder": 4,
    "size": 332568,
        }
Fri = {
    "mark": "Fri",
    "file": 4,
    "folder": 4,
    "size": 332568,
        }
Sat = {
    "mark": "Sat",
    "file": 4,
    "folder": 4,
    "size": 332568,
        }
Sun =  {
    "mark": "Sun",
    "file": 0,
    "folder": 0,
    "size": 0,
        }
week_list = [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
def target_week():
    now_week = week_current()
    print(now_week)
    for i in week_list:
        if i["mark"] == now_week:
            return i
            break
        else:
            pass
cu = target_week()
print(cu["file"] + cu["folder"])
"""

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


x = 1
delete_flag = 0
copy_flag = 0
check_flag = 0
week_current = "Mon"
for i in range(5):
    print("Execute " + str(x) + " Times")
    stop_time = 230700
    print("current_time is: " + str(stop_time))
    if 0 < stop_time < 10000 and week_current == "Sat":
        print("delete time is coming up, stop testing")
        if delete_flag == 0:
            print("dele1")
            delete_flag = delete_flag + 1
        else:
            print("Already deleted folder")
    elif 0 < stop_time < 10000 and week_current != "Sun":
        print("copy time is coming up, stop testing")
        if copy_flag == 0:
            print("copy1")
            copy_flag = copy_flag + 1
        else:
            print("Already copy data")
    elif 230000 < stop_time:
        print("Check time, start to check")
        ui_result = 1
        if check_flag == 0:
            if ui_result == 1:
                print("check1")
                check_flag = check_flag + 1
            elif ui_result == 2:
                print("Still syncing...")
            else:
                print("break")
                break
        else:
            print("Already check data") 
    else:
        delete_flag = 0
        copy_flag = 0
        check_flag = 0
    x = x + 1
    print("wait")