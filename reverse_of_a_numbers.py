n=int(input())
s=0
while n>0:
    temp=n%10
    s=s*10+temp
    n=n//10
print(s)
