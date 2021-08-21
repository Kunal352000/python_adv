"""
working with builtins module:
-----------------------------
    builtins is one builtin module in python,we can access the builtins module
    properties directly wihout importing builtins module into our program

        import builtins
        print(dir(builtin))
        """
x=[5,3,7,2]
print(x)
print(id(x))
print(type(x))
print(min(x))
print(max(x))
print(sum(x))
print(sorted(x))
print(list(reversed(x)))
y=10
print(bin(y))
print(oct(y))
print(hex(y))
print(pow(2,3))
print(ord('a'))
print(chr(65))
print(round(2.49))

