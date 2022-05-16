n=int(input())
s=0
m=0
while n:
    r=n%10
    n=n//10
    if r%2==0:
        s+=1
    else:
        m+=1
if m>0 and s>0:
    print("Mixed")
elif m>0 and s==0:
    print("Odd")
elif m==0 and s>0:
    print("Even")