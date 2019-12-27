cmd = "D:\\fciv.exe -r D:\\m1"
oo_cmd = os.popen(cmd).read()
#print(oo_cmd)
a = oo_cmd.split("\n")
print(a)
che_list = []
start_flag = 0
for i in a:
    # print(i,a.index(i))
    if "Start Time" in i:      
        add_flag = a.index(i)
        start_flag = 1
        print("start_flag:" + str(start_flag))
    elif "End Time" in i:
        break
    elif start_flag == 1 and a.index(i) > add_flag:
        if i != "":
            i = i.split(" ")
            che_list.append(i[0])
    else:
        print("pass")
print(che_list)
#index = vowels.index('e')
#print('The index of e:', index)