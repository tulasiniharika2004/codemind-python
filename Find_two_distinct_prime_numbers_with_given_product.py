def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
if is_prime(n)==1:
    print(-1)
else:
    for i in range(1,n):
        if n%i==0:
            if is_prime(i) and is_prime(n//i):
                print(i,n//i)
                break