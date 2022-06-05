def f(n,x=68):
    s=''
    while x>0:
        s+=str(x%n)
        x//=n
    return s[::-1]

for n in range(3,10):
    if f(n)[-1]=='2' and len(f(n))==4:
        print(n)
