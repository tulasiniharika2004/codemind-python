n=int(input())
s=0
sq=n*n
while(sq):
    r=sq%10
    s+=r
    sq=sq//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")