from sikuli import *
from library_qsync import *

def get_os_ver():
    os_dir = os.popen("ver").read()
    print(os_dir)
    os_split = os_dir.split("[")
    print(os_split)
    os_split1 = os_split[1].split(" ")
    print(os_split1)
    os_split2 = os_split1[1].split(".")
    if os_split2[0] == "10":
        print("Win10")
        return "Win10"
    elif os_split2[0] == "6":
        print("Win7")
        return "Win7"
    else:
        print("Unknown OS")
        return "Unknown OS"
def set_browser_sty():
    if get_os_ver() == "Win10":

        check_region = Region(59,7,273,44)
        
        check_region.click(Pattern(search_path("view_tab")).similar(0.70))
        wait(2)
        click(Pattern(search_path("big_view_button")).similar(0.70))
        wait(2)
        click(Pattern(search_path("browser_window_button")).similar(0.70))
    elif get_os_ver() == "Win7":
        type("v", KeyModifier.ALT)
        wait(1)
        type("r", KeyModifier.SHIFT)
        wait(1)
        type(Key.ENTER)
        wait(1)
        click(Pattern(search_path("manager_button")).similar(0.70))
        wait(1)
        click(Pattern(search_path("configuration_button")).similar(0.70))
        wait(1)
    else:
        print("Failed")

    wait(2)
    if exists(Pattern(search_path("show_browser_window")).similar(0.90)):
        print("browser window opened status")
        click(Pattern(search_path("show_browser_window")).similar(0.90))
    elif exists(Pattern(search_path("hide_browser_window")).similar(0.90)):
        print("browser window closed status")
        type(Key.ENTER)
    else:
        print("set browser failed")

type("r", KeyModifier.WIN)
wait(1)
type("C:\\Users\\User\\Qsync\\dd")
wait(1)
type(Key.ENTER)
wait(1)
type(Key.UP, KeyModifier.WIN)
wait(1)
set_browser_sty()

data_items = 68

if exists(Pattern(search_path("syncdone_item_icon")).similar(0.70)):
    pass
    flag = 1
else:
    flag = 0
assert flag == 1, "not find syncdone icon"
a = findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
b = []
for i in a:
    b.append(i)
print(len(b))

if data_items <= 33:
    print("number: " + str(len(b)))
elif data_items > 33:
    de = (data_items-33)/11
    be = (data_items-33)%11
    if be != 0:
        for i in range(de+1):
            print(de+1)
            wait(1)
            click_region = Region(1253,625,27,36)
            click_region.click(Pattern(search_path("down_button")).similar(0.70))


            xregion = Region(7,526,1247,127)
            c = xregion.findAll(Pattern(search_path("syncdone_item_icon")).similar(0.70))
            d = []
            for i in c:
                d.append(i)
            print(len(d))


