from calendar import month,TextCalendar,TUESDAY
year=int(input("Enter the year: "))
mon_num=int(input("Enter the month number: "))
print(month(year,mon_num))
print('*'*20)
c=TextCalendar(TUESDAY)
print(c.formatmonth(year,mon_num))
