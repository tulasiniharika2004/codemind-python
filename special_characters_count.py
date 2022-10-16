s=input().lower()
c=0
for i in s:
    if i not in ' abcdefghijklmnopqrstuvwxyz':
        c+=1
print(c)        