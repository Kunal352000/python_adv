"""
mixing of default and non-default arguments
"""
def add(x=1,y):
    z=x+y
    print(z)
add(2,2)
"""
we recive syntaxError becoz non default argumnets follows default arguments

we can pass first as a non default and pass the second as default is true

if we can pass first as a default and second one as non-default then we get
syntax error"""
