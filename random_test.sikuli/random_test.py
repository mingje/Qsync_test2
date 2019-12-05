import random
mark_list = ["abc"]
if len(mark_list) == 1:
    ran_list = mark_list
else:
    ran_list = random.sample(mark_list, 2)
for i in ran_list: 
    print(i)

    
b = [12,1,3]
def a(ran_switch, ran_no, *args):
    if isinstance(args[0], list) == True:
        args = args[0]
    else:
        args = args
    # decide run_list
    if ran_switch == "Y":
        if len(args) == 1:
            run_list = random.sample(args, 1)
        else:
            run_list = random.sample(args, ran_no)
    else:
        run_list = args 
        ran_no = 1
    for i in run_list:
        print(i)
df = a('Y', 2, b)  



"""
a = 'QW'
print(isinstance(a,int))
"""