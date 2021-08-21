"""wap to rename and directory in python"""
import os
print('Before:',os.getcwd())
os.chdir('vagdevi')
print('After:',os.getcwd())
print(os.listdir())
print('*'*20)
os.rename('django','dj')
os.rename('sample.py','sam.py')
os.rename('welcome.html','welcome.py')
print(os.listdir())
