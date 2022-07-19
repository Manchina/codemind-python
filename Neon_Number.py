n=int(input())
s=0
sq=n*n
while(sq>0):
      t=sq%10
      s=s+t
      sq=sq//10
if(s==n):
      print("Neon Number")
else:
      print("Not Neon Number")