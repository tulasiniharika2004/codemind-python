n=input().lower()
temp=[]
for i in n:
    if i not in temp and i!=" ":
        temp.append(i)
        temp.sort()
for i in temp:
    print(i,end='')