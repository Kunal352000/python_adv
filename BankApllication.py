import sys
class customer:
    """Customer class bank realted options"""
    bankname="KIB"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        print("After deposit your balnace:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficinet fund....can't perform this operation!")
            sys.exit()
        else:
            self.balance=self.balance-amt
            print("After withdraw your balanace:",self.balance)
print("Welcome to our KIB bank.")
n=input("Enter your name: ")
c=customer(n)
while True:
    print("\t\td-deposit\n\t\tw-withdraw\n\t\te-exit")
    option=input("Enter your option:").casefold()
    if option=="d":
        amt=float(input("Enter amount to deposit:"))
        c.deposit(amt)
    elif option=='w':
        amt=float(input("Enter amount to withdraw:"))
        c.withdraw(amt)
    elif option=='e':
        print("Thanks for using my aplication:")
        sys.exit()
    else:
        print("Choose valid option")
