def f(x,n):
    if x>n or x==13:
        return 0
    if x==n:
        return 1
    if x<n:
        return f(x+1,n)+f(x+2,n)+f(x*3,n)

print(f(1,10)*f(10,15))