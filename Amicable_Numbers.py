n=int(input())
m=int(input())
a=0
b=0
for i in range(1,n):
    if n%i==0:
        a+=i
for j in range(1,m):
    if m%j==0:
        b+=j
if a==m and b==n:
    print("Amicable")
else:
    print("Not Amicable")