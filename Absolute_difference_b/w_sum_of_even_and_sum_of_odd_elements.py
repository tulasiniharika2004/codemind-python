n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in range(0,len(l)):
    if l[i]%2==0:
        es+=l[i]
    else:
        os+=l[i]
a=abs(es-os)
print(a)