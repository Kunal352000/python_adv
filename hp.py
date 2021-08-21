from itertools import combinations
x=input("enter a string: ")
count=0
comb=combinations(x,3)
"""for i in list(comb):
    a=''.join(i)
    if a=="HSL":
        count+=1
        print(count)
"""
for i in comb:
    print(i)

