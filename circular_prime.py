def is_prime(l):
    if l==1:
        return 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            return 0
    return 1
n=int(input())
v=str(n)[::-1]
o=int(v)
if is_prime(n):
    if is_prime(n) and is_prime(o):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')