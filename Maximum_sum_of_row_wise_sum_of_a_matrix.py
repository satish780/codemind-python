a,b=map(int,input().split())
l=[]
s=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
for i in l:
    s.append(sum(i))
print(max(s))
    

    