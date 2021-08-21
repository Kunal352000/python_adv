"""wap to remove directory and file"""
import os
print(os.getcwd())
os.chdir('vagdevi')
print(os.getcwd())
print(os.listdir())
os.rmdir('dj')
print('remove directory sucessful')
os.remove('sam.py')
print('Remove file sucessfully')
print(os.listdir())
