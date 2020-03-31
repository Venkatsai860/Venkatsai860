y=input("enter the string")
#y=set(y)
z=sorted(set(y), key=y.index)
y=list(z)
Str = ' '.join(map(str, y))
print(Str)
        
