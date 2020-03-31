lst=["v","e","n","k","a","t"]
letter=str()
count=0
for i in lst:
    if count%2==0:
        
        letter=letter+(i.upper())
    else:
        letter=letter+(i)
    count+=1
print(letter)
    
        
