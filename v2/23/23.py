def f(x,n):
    if x>n or x==29:
        return 0
    if x == n:
        return 1
    return f(x+1,n)+f(x*2,n)+f(x*3,n)

print(f(2,13)*f(13,44))