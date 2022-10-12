n=input().lower()
a=[]
c=0
for i in n:
    a.append(i)
for i in a:
    if(a.count(i)==1 and i!=" "):
        c+=1
print(c)        