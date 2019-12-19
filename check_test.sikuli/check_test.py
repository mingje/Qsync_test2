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

def outut_page_items():
    current_icon_list = []
    try:
        icon_findall = findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
        for i in icon_findall:
            current_icon_list.append(i)
    except:
        current_icon_list = []
    print("current page icon: " + str(len(current_icon_list)))
    return len(current_icon_list)

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

def check_icon_result(data_items, row_items, page_item_no):
    if data_items == page_item_no:
        print("Icon check PASS: " + str(page_item_no))
        flag = 1
    elif data_items < page_item_no: 
        print("Icon check fail")
        flag = 2
    else:
        if page_item_no % row_items == 0 and data_items > row_items * 3:
            flag = 0
        else:
            print("Icon check fail")
            flag = 3
    return flag

def down_icon_check(data_items, row_items ,page_item_no):
    quotient = data_items / row_items
    remainder = data_items % row_items
    exclude_no = page_item_no / row_items
    if remainder == 0:
        down_time = quotient - exclude_no + 1
    else:
        down_time = quotient - exclude_no + 2
    print("Max down times is: " + str(down_time))
    result_icon = 0
    for i in range(down_time):
        click_region = Region(1253,625,27,36)
        click_region.click(Pattern(search_path("down_button")).similar(0.70))
        add_item_no = output_line_items()
        result_icon = result_icon + add_item_no
        if add_item_no != row_items:
            break
        else:
            print(result_icon)
    total_no = page_item_no + result_icon
    if total_no > data_items:
        total_final = total_no -11
    else:
        total_final = total_no
    print("first" + str(page_item_no))
    print("add items: " + str(result_icon))
    print("Total number: " + str(total_no))
    print("Final total number: " + str(total_final))
    return total_final



def check_icon_no_N(data_items, row_items):
# get items at first page
    x = 0
    flag = 0
    for i in range(2):
        if x == 0:
            first_page_item_no = outut_page_items()
            page_item_no = first_page_item_no
            print("First page icon no= " + str(first_page_item_no))
        else:
            page_item_no = down_icon_check(data_items, row_items, first_page_item_no)
        icon_result = check_icon_result(data_items, row_items , page_item_no)
        if icon_result == 1:
            print("End icon check: Result PASS")
            flag = 1
            break
        elif icon_result == 0:
            print("Enter advanced check step")
            flag = 0
        else:
            print("End icon check: Result FAIL")
            flag = 0
            break
        x = x + 1
    return flag

data_items = 109
row_items = 11

print(check_icon_no_N(50, 11))



"""
quotient = data_items / row_items
remainder = data_items % row_items
exclude_no = first_page_item_no / row_items
if remainder == 0:
    down_time = quotient - exclude_no + 1
else:
    down_time = quotient - exclude_no + 2
print("Max down times is: " + str(down_time))
result_icon = 0
for i in range(down_time):
    click_region = Region(1253,625,27,36)
    click_region.click(Pattern(search_path("down_button")).similar(0.70))
    add_item_no = output_line_items()
    result_icon = result_icon + add_item_no
    if add_item_no != row_items:
        break
    else:
        print(result_icon)
total_no = first_page_item_no + result_icon
if total_no > data_items:
    total_finall = total_no -11
else:
    total_finall = total_no
print("add items: " + str(result_icon))
print("Total number: " + str(total_no))
print("Finall total number: " + str(total_finall))
"""


############################
"""
x = 0
for i in range(15):
    if x == 0:
        page_item_no = outut_page_items()
        first_page_item_no = page_item_no
        print("First page icon no= " + str(first_page_item_no))
    else:
        add_item_no = output_line_items()
        print("Add no = " + str(add_item_no))
        page_item_no = add_item_no + page_item_no
    
    if page_item_no > data_items:
        page_item_no = page_item_no - row_items
    else:
        pass
    
    print("Current icon = " + str(page_item_no))
    x = x + 1    
    if data_items == page_item_no:
        print("Check PASS: " + str(page_item_no))
        break
    elif data_items < page_item_no:
        check_point = page_item_no - row_items
        if check_point > data_items:
            print("Check fail")
            break
        else:
            pass
    elif data_items > page_item_no:
        try:
            click_region = Region(1253,625,27,36)
            click_region.click(Pattern(search_path("down_button")).similar(0.70))
        except:
            print("Check fail")
            break
    else:
        print("Unknow status")
        break
"""





"""    
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

