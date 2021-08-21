from calendar import isleap
year=int(input("Enter your year: "))
if isleap(year):
    print("{} year is leap ".format(year))
else:
    print("{} year is not leap".format(year))
