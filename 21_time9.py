"""
strftime():
-----------
    to convert a time in tuple fromat into string according to our
    sepcifications
        strftime(format,[time in tuple])"""
import time
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%a %Y-%m-%d %H:%M:%S %p',time.gmtime()))
print(time.strftime('%A %Y-%B-%d %H:%M:%S %p'))
print(time.strftime('%A %y-%b-%d %I:%M:%S %p'))
"""
output:
-------
2021-07-21
2021-07-21 16:18:48
Wed 2021-07-21 10:48:48 AM
Wednesday 2021-July-21 16:18:48 PM
Wednesday 21-Jul-21 04:18:48 PM
"""
