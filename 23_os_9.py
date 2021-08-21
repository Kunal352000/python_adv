"""wap to return the lsit of all the items(files and directories) in the specified
location?"""
import os
print("Before: ",os.getcwd())
os.chdir('vagdevi')
print("After: ",os.getcwd())
print(os.listdir())
print('*'*20)
print(os.listdir('E:\\krishna\\guido'))
"""
output:
-------
Before:  C:\Users\Dell\Desktop
After:  C:\Users\Dell\Desktop\vagdevi
['addition.java', 'base.js', 'demo.py', 'django', 'hello.txt', 'java', 'New Text Document.txt', 'python', 'sample.py', 'style.css', 'welcome.html']
********************
[]
"""
