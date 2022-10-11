n=int(input())
x=list(map(int,input().split()))
a=int(input())
for i in x:
    if i==a:
        print("True")
        break
else:
    print("False")