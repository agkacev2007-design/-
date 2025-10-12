a=[123, 456, 789]
b=[]
for i in a:
    i=str(i)
    for g in i:
        b.append(int(g))
print(b)