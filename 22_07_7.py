from calendar import _premonth,_nextmonth
year=int(input("Enter the year: "))
mon_num=int(input("Enter the month: "))
print(_premonth(year,mon_num))
print(_nextmonth(year,mon_num))
