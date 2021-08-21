class Test:
    a=10#static method
    def __init__(self):
        Test.a=20#modify static variable by using classname
t=Test()
print(Test.a)#accesing static variable outside a class by using classname
print(t.a)#accesing static variale outside a class by sing reference variable

