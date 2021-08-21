"""
all()-->if all the elements are True in our iterable object then only all() to
        return True otherwise all() to return False

        --> 0 means False
        --> execept o,we can take anyvalue that treated as a True
        --> all(iterableobj)
        """
print(all([8,9.1,3j,"siva"]))#True
print(all([True,0,9,False,2+3j]))#False
print(all([0,False,True]))#False
print(all([0,False]))#false
print(all("kunal"))#True
print(all(34))#TypeError-->int is not iterable object
