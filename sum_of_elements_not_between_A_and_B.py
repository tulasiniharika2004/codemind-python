n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
s=0
for i in x:
    if i>=a and i<=b:
        c.append(i)
for i in x:
    if i in x and i not in c:
        s+=i
print(s)        
        