def prime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return 1
    return 0
n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if(i!=1 and prime(i)!=1):
        c+=1
print(c)        