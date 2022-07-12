n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=0
for i in range(0,len(l)):
    if(l[i]<=m):
        s+=l[i]
print(s)        
