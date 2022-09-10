a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i==1):
        continue
    c=0
    for j in range(2,i+1):
        if(i%j==0):
            c+=1
    if(c<2):
       print(i)
