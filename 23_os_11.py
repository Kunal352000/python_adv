"""wap to print only file name from the given specified location"""
import os
print(os.getcwd())
os.chdir('vagdevi')
for i in os.listdir():
    if os.path.isfile(i):
        print(i)
"""
output:
-------
C:\Users\Dell\Desktop
addition.java
base.js
demo.py
hello.txt
New Text Document.txt
sample.py
style.css
welcome.html
"""

