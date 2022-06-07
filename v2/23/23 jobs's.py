def f(x,n):
    if x>n: return 0
    if x==n: return 1
    if x<n:
        return f(x+2,n)+f(x*2,n)

    
print(f(1,18)*f(18,52))