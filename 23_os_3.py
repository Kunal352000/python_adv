#wap to make/create a directory
import os
print("Before",os.getcwd())
os.mkdir('vagdevi1')
print("Directory created sucessfully in %s"%os.getcwd())
os.chdir('E:\\krishna')
os.mkdir('E:\\krishna\\guido')
print("Directory created sucessfully in %s"%os.getcwd())
"""
output:
------
Before C:\Users\Dell\Desktop
Directory created sucessfully in C:\Users\Dell\Desktop
Directory created sucessfully in E:\krishna
"""
