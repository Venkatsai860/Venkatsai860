a=input("enter the alphabets")
b=len(a)
lst=list(a)
sen=lst[1:b+1]
pj=ord(lst[b-1])+1
x=list(chr(pj))
#print(x)
y=sen+x

z=' '.join(map(str,y))
print(z)


