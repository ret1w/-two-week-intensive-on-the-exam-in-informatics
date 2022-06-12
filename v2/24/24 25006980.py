s=open("24 25006980.txt").read()
for j in "QWERTYUIOPASDFGHJKLZXCVBNM":
    s=s.replace(f"Z{j}RO","Z*RO")
print(s.count("Z*RO"))