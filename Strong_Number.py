n=int(input())
temp=n
s=0
while(n!=0):
    fact=1
    rem=n%10
    while(rem!=0):
        fact=fact*rem
        rem=rem-1
    s=s+fact
    n=n//10
if(temp==s):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")
