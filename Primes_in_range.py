def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=0
for j in range(n,m+1):
    if prime(j):
        c+=1
print(c)        