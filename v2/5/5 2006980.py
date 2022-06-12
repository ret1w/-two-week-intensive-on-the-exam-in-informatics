for i in range(1,10000):
    m=bin(i)[2:]
    for j in range(2):
        if m.count("1")%2==0:
            m=m+'0'
        else:
            m+="1"
    R=int(m,2)
    if R>103:
        print(i)