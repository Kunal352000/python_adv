from calendar import isleap
year=int(input("Enter the year: "))
if isleap(year):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
