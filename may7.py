n=[1,2,3,4,5]
def int_(n):
    summa=0
    for i in range(len(n)):
        n[i]=n[i]*1.1
    return n
print(int_(n))