n=input()
b=list(n)
s=0
for i in n:
    if(n.count(i)==1):
        print(i)
        s=1
        break
if(s==0):
    print("-1")