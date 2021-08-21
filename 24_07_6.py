from calendar import leapdays
syear=int(input("Enter the starting year: "))
eyear=int(input("Enter the ending year: "))
print(leapdays(syear,eyear+1))
