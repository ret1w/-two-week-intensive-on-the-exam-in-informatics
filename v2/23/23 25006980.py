def f(s,n):
    if s>n: return 0
    if s==n: return 1
    if s<n:
        return f(s+1,n)+f(s*3,n)


print(f(1,30)*f(30,50)*f(50,150))
