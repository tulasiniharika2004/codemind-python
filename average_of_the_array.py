n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    s+=i
    avg=s/n
print("{:.2f}".format(avg))    