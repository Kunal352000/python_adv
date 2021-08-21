from calendar import leapdays
syear=int(input("Enter starting year: "))
eyear=int(input("Enter ending year: "))
print(leapdays(syear,eyear+1))
