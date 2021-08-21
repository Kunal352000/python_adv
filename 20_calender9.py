from calendar import isleap
syear=int(input("Enter your year: "))
eyear=int(input("Enter end year: "))
for i in range(syear,eyear+1):
    if isleap(i):
        print(i)
