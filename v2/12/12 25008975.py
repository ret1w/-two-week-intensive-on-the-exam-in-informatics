s='7'*170
while '777'in s:
    s=s.replace('77','2',1)
    s=s.replace('22','7',1)
print(s)