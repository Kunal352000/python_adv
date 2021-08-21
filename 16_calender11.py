from calendar import month,HTMLCalendar
year=int(input("Enter the year: "))
mon_num=int(input("Enter month number: "))
print(month(year,mon_num))
print("*"*20)
c=HTMLCalendar()
print(c.formatmonth(year,mon_num))
