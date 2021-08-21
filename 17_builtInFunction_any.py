"""
any()--->if any one element is True then only any() to return True otherwise
         any() to return False
"""
print(any([8,9.1,3j,"kunal"]))#True
print(any([7,0,8,3]))#True
print(any([True,0,9,False,2+3j]))#True
print(any(('a',False,True)))#True
print(any([0,False]))#false
print(any("kunal"))#true
print(any(1111))#int object ius not iterable
