from calendar import isleap
syear=int(input("Enter starting year: "))
eyear=int(input("Enter ending year: "))
for i in range(syear,eyear+1):
    if isleap(i):
        print(i)
