def add_digit(n):
    sum=0
    while n!=0:
        r=n%10
        sum+=r
        n//=10
    if sum>=0 and sum<=9:
        return sum
    else:
        return add_digit(sum)
n=int(input())
print(add_digit(n))