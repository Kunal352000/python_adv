import itertools
shivani=input("Enter your string: ").upper()
c1=list(itertools.combinations(shivani,3))
dad=(c1.count(('d','a','d')))
mom=(c1.count(('m','o','m')))
print(dad+mom)
