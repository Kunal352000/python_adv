"""
python dont support function overloading concept beaacuse our python interpreter
to understand/recoginize last defined function only
"""
def f1(*x):
    if len(x)==0:
        print("hey")
    if len(x)==1:
        print("kunal")
    if len(x)==2:
        print("good mmorning")
f1()
f1(2)
f1(2,3)
"""
output:
-------
hey
kunal
good mmorning
"""
