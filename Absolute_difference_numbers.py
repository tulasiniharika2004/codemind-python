a,b=map(int,input().split())
l=a%(10**b)
o=str(a)[::-1]
p=int(o)%(10**b)
v=str(p)[::-1]
print(abs(l-int(v)))