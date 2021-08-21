import builtins
x=(dir(builtins))
for i in x:
    if i[0].islower():
        print(i,end=" ")
