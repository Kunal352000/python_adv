#wap to change the directory
import os
print("Before -->",os.getcwd())
os.chdir('os')
print("After: -->",os.getcwd())
#output
#Before --> C:\Users\Dell\Desktop
#After: --> C:\Users\Dell\Desktop\os
