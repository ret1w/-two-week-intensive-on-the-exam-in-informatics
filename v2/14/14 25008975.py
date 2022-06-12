x=17*16**455+2**67-4**47+58
d=oct(x)[2:]
s=0
for i in "248":
    s+=d.count(i)
print(d)
print(s)