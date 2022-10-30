n=int(input())
x=list(map(int,input().split()))
y=[]
z=[]
for i in x:
    y.append(i)
for i in x:
    if i%2==0:
        z.append(i)
if(len(str(y))==len(str(z))):
    print(True)
else:
    print(False)