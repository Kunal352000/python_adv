"""wap to create a directories by using iteration"""
import os
print("Before:",os.getcwd())
os.chdir('vagdevi1')
print("current location:",os.getcwd())
for i in ['python1','django1','Guido1']:
    os.mkdir(i)
print("Directories Created sucessfully.")
