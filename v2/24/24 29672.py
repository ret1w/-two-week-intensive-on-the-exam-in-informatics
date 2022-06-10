f=open("inf_22_10_20_24.txt").readlines()



mx_count=0
for x in f:
    if x.count("E")>x.count("A"):
        mx_count+=1
print(mx_count)

