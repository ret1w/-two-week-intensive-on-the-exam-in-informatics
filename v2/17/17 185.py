f = [int(i) for i in open("", 'r')]
ans = [f[x]+f[x+1] for x in range(len(f)-1) if abs(f[x] % 10 == 7) or abs(f[x+1] % 10 == 7)]
print(len(ans),max(ans))