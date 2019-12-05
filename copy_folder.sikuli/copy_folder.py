import time
 
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
copy_path = "dir C:\\Users\\" + path_user + "\\@Qsync_test\\" + week_current
print(copy_path)
dd = "XCOPY C:\\PC1_test_files" + " C:\\Users\\" + path_user + "\\@Qsync_test\\" + week_current + "\ /I /E"
print(dd)
print(os.system(copy_path))
if os.system(copy_path) == 1:
    os.system(dd)
    print("copy folder")
else:
    print("Folder already existed")
