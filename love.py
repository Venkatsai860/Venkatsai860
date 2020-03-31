for i in range(5):
    for j in range(5):
        if(i==0 and j==1 or i==0 and j==3):
            print("*",end="")
        elif(i==1 or i==2):
            print("*",end="")
        elif(i==3 and 1<=j<=3 or i==4 and j==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()

