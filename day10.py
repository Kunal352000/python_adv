n=int(input())
ones_counter=0
highest_counter=0
while(n>0):
    if(n%2==1):
        ones_counter+=1
        if(ones_counter>highest_counter):
            highest_counter=ones_counter
    else:
        ones_counter=0
    n=n//2

print(highest_counter)
