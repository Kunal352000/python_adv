import datetime
x=datetime.datetime.now()
print(x)
print(type(x))
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.ctime())
print(x.max)
print(x.min)
print(x.strftime('%d-%m-%Y'))
"""
output:
-------
2021-07-21 16:58:14.862132
<class 'datetime.datetime'>
2021
7
21
16
58
14
862132
Wed Jul 21 16:58:14 2021
9999-12-31 23:59:59.999999
0001-01-01 00:00:00
21-07-2021
"""
