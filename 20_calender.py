"""
working with calnder module:
----------------------------
    if we want to display all the properties of calendar module by using
    following command
        import calender
        print(dir(calender))
        """
#wap to print particular year calender
from calendar import calendar
year=int(input("Enter your year: "))
print(calendar(year,m=2))
