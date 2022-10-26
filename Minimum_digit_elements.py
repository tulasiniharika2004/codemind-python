n=int(input())
x=list(map(int,input().split()))
m=min(x)
c=0
for j in x:
    if len(str(m))==len(str(j)):
        c+=1
        
print(c)
        
        