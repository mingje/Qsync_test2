attrib -s -h -r %1\*.* && del %1\*.* /q
dir %1 /ad /b /s >delbat.txt 
for /f %%i in (delbat.txt) do rd %%i /s /q 