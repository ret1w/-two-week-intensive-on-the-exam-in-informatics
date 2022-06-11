print(126789,126789//39)
for i in range(0,10):
    s=int(f'12{i}6789')
    if s%39==0:
        print(s,s//39)

for  i in range(0,10):
    for j in range(0,10):
        s = int(f'12{i}{j}6789')
        if s<=10**8 and s%39==0:
            print(s,s//39)