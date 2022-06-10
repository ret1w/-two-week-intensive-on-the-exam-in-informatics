s=open("24 2832503195017 .txt").readline()
s=s.replace("ZXY","ZYX").replace("ZYX","*")
for j in "XYZ":
    s=s.replace(j," ")
s=s.split()
print(max(s,key=len))
print(len(max(s,key=len)))