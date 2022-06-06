def f(x,n):
    if x>n: return 0
    if x==n: return 1
    if n>x: return f(x+1,n)+f(x*2,n)+f(x+3,n)

print(f(3,12)*f(12,16))