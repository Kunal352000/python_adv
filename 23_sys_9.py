"""how to exit from the process in the middle of profram"""
import sys
i=0
while i<=5:
    print("hey")
    if i==3:
        sys.exit()
    i+=1
print("bye")
