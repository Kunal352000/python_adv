import datetime
x=datetime.datetime.now()
print(x)
print(x-datetime.timedelta(days=1))
print(x+datetime.timedelta(days=1))
print(x-datetime.timedelta(hours=1))
print(x+datetime.timedelta(hours=1))
print(x-datetime.timedelta(minutes=1))
print(x+datetime.timedelta(minutes=1))
print(x-datetime.timedelta(seconds=1))
print(x+datetime.timedelta(seconds=1))
"""
output:
------
2021-07-21 17:38:05.560113
2021-07-20 17:38:05.560113
2021-07-22 17:38:05.560113
2021-07-21 16:38:05.560113
2021-07-21 18:38:05.560113
2021-07-21 17:37:05.560113
2021-07-21 17:39:05.560113
2021-07-21 17:38:04.560113
2021-07-21 17:38:06.560113
"""
