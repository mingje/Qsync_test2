from sikuli import *
from library_qsync import *

"""
# Remove nas
close_qsync()
wait(5)
open_qsync(os_bit)
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


# delete nas shared folder
xx = "rd /s/q z:\\"
try:
    os.system(xx)
    print("remove shared folder")
except:
    pass
"""
                
# login and pair sync folder
nas_lanip = sys.argv[1]
nas_ac = sys.argv[2]
nas_pwd = sys.argv[3]
"""
nas_lanip = "10.20.241.196"
nas_ac = "admin"
nas_pwd = "dqvts453bt3" 
"""
target = nas_detail(lanip = nas_lanip, ac = nas_ac, pwd = nas_pwd)
print(target)
os_ver = get_os_ver()
os_bit = get_os_bit()
 
open_qsync(os_bit)
wait(2)
if exists(Pattern(search_path("host_field")).similar(0.70)):
    login_pair(ip=target["lanip"], ac=target["ac"] , pwd=target["pwd"])
    wait(2)
else:
    print("Already login")

open_folder_cmd("C:\\Users\\DQV\@Qsync_test", os_ver)


