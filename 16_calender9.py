from calendar import _premonth,_nextmonth
year=int(input("Enter year: "))
mon_num=int(input("Enter month_name: "))
print("previous month",_premonth(year,mon_num))
print("Next month",_nextmonth(year,mon_num))
