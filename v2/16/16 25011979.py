def f(n):
    if n==1: return 1
    if n%2==0: return f(n-1)+n
    if n>1 and n%2!=0: return 2*f(n-2)


print(f(24))