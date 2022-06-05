for i in range(0,10):
    for j in range(0,10):
        anser="1234"+str(i)+"58"+str(j)+"8"
        if int(anser)%17==0:
            print(anser,int(anser)/17)