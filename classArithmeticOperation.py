class ArithmeticCalculations:
    def add(self,x,y):
        print("The sum of {} and {} = {}".format(x,y,x+y))
    def sub(self,x,y):
        print("The difference of {} and {} = {}".format(x,y,x-y))
    def mul(self,x,y):
        print("The multiplication of {} and {} = {}".format(x,y,x*y))
    def div(self,x,y):
        print("The division of {} and {} = {}".format(x,y,x//y))
a=ArithmeticCalculations()
while True:
    print("*"* 50)
    print("Select your option from following option:\n\t\t1-Addition\n\t\t2-Subtraction\
\n\t\t3-Multiplication\n\t\t4-Division\n\t\t5-Exit")
    print("*"*50)
    option=int(input("Enter your option: "))
    if option==1:
        a.add(eval(input("Input-1: ")),eval(input("Input-2: ")))
    elif option==2:
        a.sub(eval(input("Input-1: ")),eval(input("Input-2: ")))
    elif option==3:
        a.mul(eval(input("Input-1: ")),eval(input("Input-2: ")))
    elif option==4:
        a.div(eval(input("Input-1: ")),eval(input("Input-2: ")))
    elif option==5:
        break
    else:
        print("Invalid option")
print("Thankyou for using my apllication.")
