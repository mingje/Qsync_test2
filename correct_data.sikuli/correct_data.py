from sikuli import *
from library_qsync import *

dir = "dir D:\\ee"
a = os.popen(dir).read()
print(a)
