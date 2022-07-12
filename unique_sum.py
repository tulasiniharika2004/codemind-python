n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=0
for i in s:
    c+=i
print(c)    