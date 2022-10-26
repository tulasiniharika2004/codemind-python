n=int(input())
x=list(map(int,input().split()))
y=[]
d=0
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    c=x.count(i)
    if(i==c):
        d+=1
        print(i,end=" ")
if(d==0):
    print("-1")