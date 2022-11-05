def pali(a):
    a=str(a)
    t=a
    k=a[::-1]
    if t==k:
        return True
    return False

n=input()
a=n.upper()
c=0
l=list(a.split(" "))
for i in l:
    if pali(i):
        c+=1
print(c)