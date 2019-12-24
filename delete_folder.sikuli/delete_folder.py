from sikuli import *
from library_qsync import *

print(run_path())
"""
# delete_folder("D:\\test\\")
delete_folder("C:\\Users\\DQV\\@Qsync_test\\")
"""
"""
current_user = os.popen("whoami").read()
print(current_user)
r = str(current_user)
print(r)
rr = r.split("\\")
ss = rr[1]
ss = ss[0:-1]
print(ss) 
path_user = ss
dd = "rd /s/q C:\\Users\\" + path_user + "\\@Qsync_test\\"
print(dd)

try:
    os.system(dd)
except:
    pass

"""