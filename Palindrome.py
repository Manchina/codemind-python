n=int(input())
m=n
sum=0
while n:
    temp=n%10
    sum=sum*10+temp
    n=n//10
if sum==m:
    print("True")
else:
    print("False")