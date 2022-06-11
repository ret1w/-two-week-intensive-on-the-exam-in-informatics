def f(x):
    s=''
    while x>0:
        if str(x%13)=='12':s += "C"
        else: s+=str(x%13)
        x//=13
    return s[::-1]


x=2197**50-169**35-26
print(f(x))
print(f(x).count("C"))