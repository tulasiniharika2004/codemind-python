n=int(input())
l=list(map(int,input().split()))
s=0
d=0
for i in range(0,(n//2)+1):
    s+=i
for j in range((n//2)+1,n+1):
    d+=j
print(s)
print(d)