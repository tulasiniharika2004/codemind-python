n=int(input())
l=0
while n:
    r=n%10
    n=n//10
    if r>l:
        l=r
print(l)        