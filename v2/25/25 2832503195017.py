for i in range(0,10):
    for j in range(0,10):
        if int(f'12345{i}6{j}8')%17==0:
            print(int(f'12345{i}6{j}8'),int(f'12345{i}6{j}8')//17)