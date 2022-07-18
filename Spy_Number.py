n=int(input())
sum=0
pro=1
while(n>0):
   temp=n%10
   sum=sum+temp
   pro=pro*temp
   n=n//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")