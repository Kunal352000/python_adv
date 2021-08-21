"""wap to change the directory"""
import os
print("Before: ",os.getcwd())
os.chdir('os')
print("after:",os.getcwd())
