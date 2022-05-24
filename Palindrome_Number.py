n=int(input())
for i in range(n):
    n=int(input())
    re=0
    t=n
    while n:
        r=n%10
        re=re*10+r
        n=n//10
    if(re==t):
        print("True")
    else:
        print("False")
