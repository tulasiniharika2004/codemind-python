import math
def per(n):
    a=math.sqrt(n)
    b=a
    b=int(b)
    if b==a:
        return (True)
    return (False)
n=int(input())
for i in range(1,n+1):
    a=int(input())
    print(per(a))