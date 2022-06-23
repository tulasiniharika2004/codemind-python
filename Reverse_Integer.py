def rev_singed(n):
    s=0
    sign=1
    if(n<0):
        sign=-1
        n=n*-1
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if not -214783648<s<214783647:
        return 0
    return sign*s
n=int(input())
print(rev_singed(n))