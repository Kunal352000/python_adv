"""wap to print only sub-dirs names from the given specified location"""
import os
print("Before: ",os.getcwd())
os.chdir('vagdevi')
print('After:',os.getcwd())
for i in os.listdir():
    if os.path.isdir(i):
        print(i)
