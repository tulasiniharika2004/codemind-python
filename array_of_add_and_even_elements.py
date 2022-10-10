n=int(input())
x=list(map(int,input().split()))
c=[]
d=[]
for i in x:
    if(i%2!=0):
        c.append(i)
for i in x:
    if(i not in c):
        d.append(i)
z=c+d
for j in z:
    print(j,end=" ")