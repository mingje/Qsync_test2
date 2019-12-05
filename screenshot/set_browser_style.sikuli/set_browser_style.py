from sikuli import *
from library_qsync import *

check_region = Region(59,7,273,44)

check_region.click(Pattern(search_path("view_tab")).similar(0.70))
wait(2)
click(Pattern(search_path("big_view_button")).similar(0.70))
wait(2)
click(Pattern(search_path("browser_window_button")).similar(0.70))
wait(2)
if exists(Pattern(search_path("show_browser_window")).similar(0.90)):
    print("browser window opened status")
    click(Pattern(search_path("show_browser_window")).similar(0.90))
elif exists(Pattern(search_path("hide_browser_window")).similar(0.90)):
    print("browser window closed status")
else:
    print("fail")



