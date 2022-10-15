s=list(map(str,input().split()))
c=0
for i in s:
    i=i.lower()
    res=i[::-1]
    if res.lower()==i:
        c+=1
print(c)        