def luka(n):
    if n==1: return 2
    if n==2: return 1
    if n>2: return luka(n-2)+luka(n-1)


print(luka(10))