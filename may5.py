a=input()
b=input()
c=input()
if len(a)<len(b) and len(a)<len(c):
    print(a)
elif len(b)<len(a) and len(b)<len(c):
    print(b)
elif len(c)<len(b) and len(c)<len(a):
    print(c)
if  len(a)>len(b) and len(a)>len(c):
    print(a)
elif len(b)>len(a) and len(b)>len(c):
    print(b)
elif len(c)>len(b) and len(c)>len(a):
    print(c)