from sikuli import *
from library_qsync import *

def check_icon_no(data_items, row_items):
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
        print("b:" + str(len(b)))
    except:
        b = []
    page_item_no = len(b)
    d = []
    if page_item_no == 0:
        print("number: " + str(len(b)))
    elif data_items <= page_item_no:
        print("number: " + str(len(b)))
    else:
        click_region = Region(1253,625,27,36)
        if click_region.exists(Pattern(search_path("down_button")).similar(0.70)):
            for i in range(100):
            
                click_region.click(Pattern(search_path("down_button")).similar(0.70))
                wait(1)
                xregion = Region(13,562,1239,84)
                c = xregion.findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
                for j in c:
                    d.append(j)
                print(len(d))
                yregion = Region(1250,601,30,54)
                if yregion.exists(Pattern(search_path("syncdone_item_icon")).similar(0.90)):
                    print("ghh")
                    break
                else:
                    pass
        else:
            print("number: " + str(len(b)))
    ss = len(b) + len(d)
    
    if len(b) > data_items:
        print(ss)
    elif ss > data_items:
        ss = ss -row_items
        print(ss)
    else:
        print(ss)
    return ss
"""
if data_items <= page_item_no:
    print("number: " + str(len(b)))
elif data_items > page_item_no:
    de = (data_items-page_item_no)/11
    be = (data_items-page_item_no)%11
    if be != 0:
        loop_counter_no = de + 1
    else:
        loop_counter_no = de
    d = []
    for i in range(loop_counter_no):           
        print(loop_counter_no)
        wait(1)
        click_region = Region(1253,625,27,36)
        click_region.click(Pattern(search_path("down_button")).similar(0.70))


        xregion = Region(7,526,1247,127)
        c = xregion.findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
        for j in c:
            d.append(j)
        print(len(d))
"""


