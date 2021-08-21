import datetime
z=datetime.date(2000,5,3)
print(z)
print(type(z))
print(z.year)
print(z.month)
print(z.day)
print(z.ctime())
print(z.min)
print(z.max)
print(z.weekday())
"""
output:
--------
2000-05-03
<class 'datetime.date'>
2000
5
3
Wed May  3 00:00:00 2000
0001-01-01
9999-12-31
2
"""
