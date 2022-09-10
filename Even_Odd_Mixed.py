n=int(input())
odd=0
even=0
while(n!=0):
    rem=n%10
    n=n//10
    if(rem%2==0):
        even+=1
    else:
        odd+=1
if(even>0 and odd>0 ):
    print("Mixed")
elif(odd==0 and even>0):
    print("Even")
else:
    print("Odd")
    