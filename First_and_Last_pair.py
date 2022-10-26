n=int(input())
x=list(map(int,input().split()))
i=0
y=[]
while i!=n//2:
    y.append(x[i])
    y.append(x[(n-1)-i])
    i+=1
if len(x)%2!=0:
    y.append(x[i])
    y.append(0)
print(*y)    