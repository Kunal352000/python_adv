from calendar import isleap
year=int(input("Enter a year: "))
if isleap(year):
    print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))
