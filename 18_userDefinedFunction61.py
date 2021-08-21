"""
create a normal function to perform a arthimetic operation"""
def arith_cal(x,y):
    return x+y,x-y,x*y,x/y
print(arith_cal(10,5))
"""(15, 5, 50, 2.0)"""

arith_cal1=lambda x,y:(x+y,x-y,x*y,x/y)
print(arith_cal1(12,10))
"""
output:
--------
(22, 2, 120, 1.2)
"""
