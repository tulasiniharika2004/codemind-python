n=int(input())
x=list(map(int,input().split()))
m=max(x)
c=0
for i in x:
    if(len(str(m))==len(str(i))):
        c+=1
print(c)        
    