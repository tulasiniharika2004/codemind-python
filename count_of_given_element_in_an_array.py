n=int(input())
x=list(map(int,input().split()))
a=int(input())
c=0
for i in x:
    if i==a:
        c+=1
print(c)