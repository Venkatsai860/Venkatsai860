m=int(input("enter number"))
for i in range(m):
    for j in range(m):
        #print("+",end="")
    #print()
        if(i==0 or j==0 or i==m-1 or j==m-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
