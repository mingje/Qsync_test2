import time
from sikuli import *
from library_qsync import *
 
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
q = localtime.split(" ")
week_current = q[0]
current_user = os.popen("whoami").read()
print(current_user)
r = str(current_user)
print(r)
rr = r.split("\\")
ss = rr[1]
ss = ss[0:-1]
print(ss) 
path_user = ss
copy_path = "C:\\Users\\" + path_user + "\\@Qsync_test\\" + week_current
copy_path_cmd = "dir " + copy_path
print(copy_path_cmd)
dd = "XCOPY C:\\PC1_test_files" + " C:\\Users\\" + path_user + "\\@Qsync_test\\" + week_current + "\ /I /E /Y"
print(dd)
print(os.system(copy_path))
if os.system(copy_path) == 1:
    os.system(dd)
    print("copy folder")
else:
    print("Folder already existed")
    
# output checkksum file
output_checksum_file(copy_path)
week_info = week_current()
file = "checksum_" + week_info + ".txt"
from_path = os.getcwd() + "\\" + file
to_path = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\"
copy_file(from_path, to_path, file)
