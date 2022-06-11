s=open("24 25011999.txt").readline()
s=s.replace("BB",'DD').replace("DD","*")
for x in "ABD":
    s=s.replace(x," ")
s=s.split()
print(len(max(s,key=len)))