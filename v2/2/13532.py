print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not z) and ((not x) or y):
                print(x,y,z)