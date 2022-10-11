n=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    if(i%2!=0):
        c.append(i)
print(c[-1])        