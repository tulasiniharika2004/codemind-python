lower_value=int(input())
upper_value=int(input())
for n in range(lower_value,upper_value):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)