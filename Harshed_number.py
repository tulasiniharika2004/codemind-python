n=int(input())
s=0
t=n
while n:
    r=n%10
    s+=r
    n=n//10
if t%s==0:
    print(True)
else:
    print(False)