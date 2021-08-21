from calendar import leapdays
syear=int(input("Enter the starting year: "))
eyear=int(input("Enter the ending year:"))
print("The no. of leapdays b/w {} and {} are {} days".format(syear,eyear,
                                                        leapdays(syear,eyear+1)))
