def ss(str1):
    if len(str1)==0:
        return [" "]
    small=ss(str1[1:len(str1)])
    result=[" "]*(2*len(small))
    k=0
    for i in range(len(small)):
        result[k]=small[i]
        k+=1
    for i in range(len(small)):
        result[k]=str1[0]+small[i]
        k+=1
    return result
kunal=(ss('momodaamad'))
#print(kunal)
print('dad'in kunal)
print(len('mom' in 'momodaamad'))
