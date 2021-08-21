import itertools
x='momodaamad'
seq=[]
for i,j,k in itertools.combinations(x,3):
    seq.append(i+j+k)
#print(seq)

#print(seq.count(('mom')))
#print(seq.count(('dad')))
print(seq.count(('mom'))+seq.count(('dad')))
