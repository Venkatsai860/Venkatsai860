for i in range(7):
    for j in range(7):
        if(i==0 or i==6):
            print("*",end="")
        elif(j==0 and i<3 or i==3 or j==6 and i>3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
