
def get_pc_user_name(info_name):
    info_name_list = []
    pc_info = os.popen("whoami").read()
    pc_info_list = pc_info.split("\\")
    pc_name = pc_info_list[0]
    user_name = pc_info_list[1]
    user_name = user_name[0:-1]
    if info_name == "pc_name":
        return pc_name
    else:
        return user_name

def open_folder(folder_path):
    type("r", KeyModifier.WIN)
    wait(1)
    if folder_path == "default":
        path = "C:\\Users\\" + get_pc_user_name(user_name) + "\\Qsync\\"
    else:
        path = folder_path
    type(path)
    type(Key.ENTER)
    wait(3)
    type(Key.UP, KeyModifier.WIN)

open_folder(folder_path = "D:\\test")       
"""
open_folder(folder_path = "default")
rightClick("1572422143831.png")
wait(1)
hover("1572422335523.png")
wait(1)
type(Key.DOWN)
type(Key.DOWN)
type(Key.ENTER)

        
def checkbox_no():
    try:
        c = findAll("1572492372069.png")
        d = []
        for i in c:
            d.append(i)
        return len(d)
    except:
        return 0


a = findAll("1572492103478.png")
z = 0
for j in a:
    click(j)
    z = z + 1
    wait(2)
    if checkbox_no() > z:
        print("select all")
        break
    else:
        print("not select yet")
type(Key.ENTER)
waitVanish("1572427525514.png",120)
wait(3)

click("1572492515839.png")
wait(5)
click("1572492588442.png")
wait(1)
click("1572492615774.png")
wait(3)
type(Key.F4, Key.ALT)
        

click("1572492515839.png")
wait(5)
click("1572504810362.png")
wait(1)
type(Key.RIGHT)
wait(1)
click("1572504910752.png")
type(Key.TAB)
wait(2)
type(Key.ENTER)
wait(2)
if exists("1572505062213.png"):
    print("accept team shared folder success")
else:
    print("accept team shared folder failed")

"""