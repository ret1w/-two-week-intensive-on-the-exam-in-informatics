n=2
n=bin(n)[2:]
if int(n) % 2 == 0:
    print(n)
    print(sum(list(map(int,[j for j in n]))))