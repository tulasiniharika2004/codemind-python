def prime(n):
    if n==1:
        return(False)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    r=0
    v=0
    while(n):
        d=n%10
        if prime(d):
            r+=1
        v+=1    
        n=n//10
    if(v==r):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")