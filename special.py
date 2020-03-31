
import re
n=input("enter the string")
x=re.sub('[^A-Za-z]+', '', n)
print(x)
