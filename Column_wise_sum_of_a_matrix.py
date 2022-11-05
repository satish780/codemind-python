a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
d=[]
for j in range(b):
    c=0
    for m in range(len(l)):
        c +=l[m][j]
    d.append(c)
print(*d)
    