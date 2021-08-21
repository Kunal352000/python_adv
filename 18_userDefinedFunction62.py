"""
create a normal function to check wheather given number is positive or
negative or zero?"""
num=int(input("Enter your number: "))
def check(x):
    if x>0:
        return 'positive'
    elif x<0:
        return 'negative'
    else:
        return 'zero'
print(check(num))

num1=int(input("Enter your number: "))
pnz=lambda x: 'positive'if x>0 else 'negative' if x<0 else 'zero'
print(pnz(num1))
