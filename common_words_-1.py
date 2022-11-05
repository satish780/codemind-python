a=input()
a=a.lower()
b=input()
b=b.lower()
l=list(a.split())
m=list(b.split())
c=0
for i in l:
    if i in m:
        c+=1
print(c)