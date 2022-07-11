n=input()
i=list(n)
s=set(i)
if len(i)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")