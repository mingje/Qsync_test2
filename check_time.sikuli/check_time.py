from sikuli import *
from library_qsync import *


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

"""
data_items = 110
row_items = 11
a = data_items / row_items
b = a-1
first = 33
print(b)
x = 0
for i in range(b):
    click_region = Region(1253,625,27,36)
    click_region.click(Pattern(search_path("down_button")).similar(0.70))
    v = output_line_items()
    if x == 0:
        gg = first
    else:
        gg = gg + v
        
    if v != row_items:
        if gg > data_items:
            gg = gg - row_items
            break
    else:
        pass
    x = x + 1
    print(gg)
print("total:" + str(gg))
"""
dir_cmd = "dir D:\\test"
dir_result = os.popen(dir_cmd).read()
