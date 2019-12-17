from sikuli import *
from library_qsync import *


def counter_surplus_no(data_type, counter_type, path):
    try:
        surplus_no = counter_data(data_type, counter_type, path)
    except:
        surplus_no = 0
    return surplus_no

path1 = "C:\\Users\\" + get_pc_info("user_name") + "\\@Qsync_test\\.qsync" 
path = "D:\\test"

print(counter_surplus_no("total", "all", path1))