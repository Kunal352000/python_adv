s=lambda a,b:a if a>b else b
print("The biggest of {} and {} is {}".format(12,13,s(12,13)))
print("The biggest of {} and {} is {}".format(15,16,s(15,16)))
print("The biggest of {} and {} is {}".format(16,17,s(16,17)))
"""
output:
-------
The biggest of 12 and 13 is 13
The biggest of 15 and 16 is 16
The biggest of 16 and 17 is 17
"""
