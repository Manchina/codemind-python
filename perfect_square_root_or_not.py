n=int(input())
import math
s=math.sqrt(n)
y=s-math.floor(s)
if y==0:
    print("True")
else:
    print("False")