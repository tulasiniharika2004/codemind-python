n=int(input())
x=list(map(int,input().split()))
for i in range(len(x)-1,-1,-1):
    if(x[i]%2!=0):
        print(i)
        break