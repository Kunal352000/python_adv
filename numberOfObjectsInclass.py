class Test:
    count=0
    def __init__(self):
        Test.count+=1
    @classmethod
    def detNoOfObjects(cls):
        print("The number of objects created:",cls.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.detNoOfObjects()
