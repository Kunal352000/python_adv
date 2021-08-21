"""to kill the parent process"""
import os
print(os.kill(os.getppid(),1))
