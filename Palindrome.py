n=int(input())
t=n
rev=0
while(t!=0):
    rem=t%10
    rev=rev*10+rem
    t=t//10
if n==rev:
    print("True")
else:
    print("False")