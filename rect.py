m=int(input("enter rows:"))
n=int(input("enter cols:"))
for i in range(m):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==m-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
