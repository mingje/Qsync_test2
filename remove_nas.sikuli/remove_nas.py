from sikuli import *
from library_qsync import *

click(Pattern(search_path("more_button")).similar(0.70))
wait(2)
click(Pattern(search_path("removeNAS_option")).similar(0.70))
wait(2)
click(Pattern(search_path("option_button")).similar(0.70))
wait(1)
type(Key.DOWN)
wait(1)
type(Key.ENTER)
wait(1)
waitVanish((Pattern(search_path("pleasewait_string")).similar(0.70)),120)
if exists(Pattern(search_path("host_field")).similar(0.70)):
    print("Remove NAS success")
    flag = 1
else:
    flag = 0
assert flag == 1, "Remove NAS failed"

