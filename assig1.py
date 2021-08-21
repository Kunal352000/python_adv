x=['hai', 'siva','krishna', 'good', 'morning', 'where', 'are', 'you']
y=['hai', 'rama','krishna', 'good', 'evening','how', 'are', 'you']
match=[]
unmatch=[]
if x[0]==y[0]:
    match.append(x[0])
else:
    unmatch.append(x[0])
    unmatch.append(y[0])
if x[1]==y[1]:
    match.append(x[1])
else:
    unmatch.append(x[1])
    unmatch.append(y[1])
if x[2]==y[2]:
    match.append(x[2])
else:
    unmatch.append(x[2])
    unmatch.append(y[2])
if x[3]==y[3]:
    match.append(x[3])
else:
    unmatch.append(x[3])
    unmatch.append(y[3])
if x[4]==y[4]:
    match.append(x[4])
else:
    unmatch.append(x[4])
    unmatch.append(y[4])
if x[5]==y[5]:
    match.append(x[5])
else:
    unmatch.append(x[5])
    unmatch.append(y[5])
if x[6]==y[6]:
    match.append(x[6])
else:
    unmatch.append(x[6])
    unmatch.append(y[6])
if x[7]==y[7]:
    match.append(x[7])
else:
    unmatch.append(x[7])
    unmatch.append(y[7])
print(match)
print(unmatch)

