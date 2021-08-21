import datetime
y=datetime.date.today()
print(y)
print(type(y))
print(y.year)
print(y.month)
print(y.day)
print(y.ctime)
print(y.max)
print(y.min)
print(y.weekday())
print(y.strftime('%d-%m-%Y'))
"""
output:
-------
2021-07-21
<class 'datetime.date'>
2021
7
21
<built-in method ctime of datetime.date object at 0x000001C62DCAACF0>
9999-12-31
0001-01-01
2
21-07-2021
"""
