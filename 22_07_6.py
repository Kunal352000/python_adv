from calendar import isleap
syear=int(input("Enter the starting year: "))
eyear=int(input("Enter the ending year: "))
for year in range(syear,eyear+1):
    if isleap(year):
        print(year)
