from sikuli import *
from library_qsync import *



nas_lanip = sys.argv[1]
nas_ac = sys.argv[2]
nas_pwd = sys.argv[3]
reset_flag = sys.argv[4] # "Y" or "N"

"""         
nas_lanip = "10.20.241.137"
nas_ac = "qa03"
nas_pwd = "1234" 
reset_flag = "N"
"""
# define target_client
#target_client = target_client()
print(target_client())
tar = str(target_client())
print(tar)
target_client = eval(tar)

target = nas_detail(lanip = nas_lanip, ac = nas_ac, pwd = nas_pwd)
print(target)

if reset_flag == "Y":
    # Remove nas
    close_qsync()
    wait(5)
    open_qsync()
    wait(2)
    if exists(Pattern(search_path("host_field")).similar(0.70)):
        print("Already remove nas")
    else:
        remove_nas_profile()
    close_qsync()
    
    # delete sync folder
    current_user = os.popen("whoami").read()
    print(current_user)
    r = str(current_user)
    rr = r.split("\\")
    pc_name = rr[0]
    ss = rr[1]
    ss = ss[0:-1]
    path_user = ss
    dd = "rd /s/q C:\\Users\\" + path_user + "\\@Qsync_test\\"
    print(dd)
    try:
        os.system(dd)
        print("Clean up sync folder")
    except:
        pass
else:
    print("Not reset")

# login and pair sync folder
 
open_qsync()
wait(2)
if exists(Pattern(search_path("host_field")).similar(0.70)):
    login_pair(ip=target["lanip"], ac=target["ac"] , pwd=target["pwd"])
    wait(2)
else:
    print("Already login")
close_qsync()
wait(3)

 
# Open and close Qsync
x = 1                         
for i in range(200):
    print("Execute " + str(x) + " Times")
    open_qsync()
    wait(20)
    stop_time = int(time.strftime("%H%M%S"))
    print("current_time is: " + str(stop_time))
    if 210000 < stop_time < 220000 and week_current() == "Sat":
        print("delete time is coming up, stop testing")
        path = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + target_client["folder_name"] + "\\"
        delete_folder(path)
        for i in range(10):
            wait(600)
            jump_time = int(time.strftime("%H%M%S"))
            ui_result = check_main_sync()
            if ui_result == 1 and jump_time > 220000:
                close_qsync()       
                wait(2)
                break
            elif ui_result == 0:
                break
            else:
                pass
    elif 210000 < stop_time < 220000 and week_current() != "Sun":
        print("copy time is coming up, stop testing")
        path1 = "C:\\team_folder_data"
        path2 = "C:\\Users\\" + get_pc_info("user_name") + "\\Qsync\\" + target_client["folder_name"] + "\\"
        copy_data(path1, path2, "by_week")
        close_qsync()       
        wait(2)
    else:
        print("Testing time, keep going")
        ui_result= check_main_sync()
        if ui_result == 1:
            check_share_folder()
            check_team_folder()
        elif ui_result == 2:
            print("Still syncing...")
        else:
            send_mail(target_client["pc_name"])
            break
            wait(600)
            # wait(10)
            close_qsync()       
            wait(2)
    x = x + 1
    wait(600)
    # wait(10)