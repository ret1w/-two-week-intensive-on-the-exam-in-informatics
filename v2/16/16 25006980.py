def f(n):
    if n<=70: return f(n+2)+2*f(n*3)
    if n>70: return n-50

print(f(40))