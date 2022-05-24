a=int(input())
b=int(input())
p=0

s=0
for i in range(1,a):
    if(a%i==0):
        s=s+i
for j in range(1,b):
    if(b%j==0):
        p=p+j
if(p==a and s==b):
    print("Amicable")
else:
    print("Not Amicable")        