n=int(input())
s=str(n)
length=len(s)
s=0
i=1
temp=n
rev=0
while(temp!=0):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
while(rev!=0):
    rem=rev%10
    s+=rem**i
    i=i+1
    rev=rev//10
if s==n:
    print("True")
else:
    print("False")
    

    

