n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    i=str(i)
    y.append(len(i))
for i in x:
    i=str(i)
    if(len(i)==max(y)):
        print(i,end=' ')
    