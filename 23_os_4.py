"""wap to create a directory by using iteration"""
import os
print("Before:",os.getcwd())
os.chdir('vagdevi1')
print("After:",os.getcwd())
for i in ['python','django','data science']:
    os.mkdir(i)
print("Directory are created succesfully: ")
"""
output:
-------
Before: C:\Users\Dell\Desktop
After: C:\Users\Dell\Desktop\vagdevi1
Directory are created succesfully:
"""
