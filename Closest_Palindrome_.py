def id_pali(l):
    v=str(l)[::-1]
    o=int(v)
    if o==l:
        return 1
    else:
        return 0
n=int(input())
i,j=1,-1
while 1:
    if id_pali(n+i)==1:
        x=n+i
        break
    i+=1
while 1:
    if id_pali(n+j)==1:
        y=n+j
        break
    j-=1
if x-n==n-y:
    print(y,x)
elif(x-n>n-y):
    print(y)
else:
    print(x)