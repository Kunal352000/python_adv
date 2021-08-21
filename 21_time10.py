"""
strptime():
-----------
    to parse a string into time in tuple format according to our format
    specifications.
        strptime(string,format)
    """
import time
print(time.strptime('1992-01-14','%Y-%m-%d'))
"""
output:
-------
time.struct_time(tm_year=1992, tm_mon=1, tm_mday=14, tm_hour=0,
tm_min=0, tm_sec=0, tm_wday=1, tm_yday=14, tm_isdst=-1)
"""
