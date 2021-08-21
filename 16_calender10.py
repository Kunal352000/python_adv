from calendar import month,TextCalendar,SUNDAY
year=int(input("Enter year: "))
mon_num=int(input("Enter month: "))
print(month(year,mon_num))
print('*'*20)
c=TextCalendar(SUNDAY)
print(c.formatmonth(year,mon_num))
