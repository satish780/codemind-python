n,m=map(int,input().split())
l=[]
for i in range(n):
    k=list(map(int,input().split()))
    l.append(k)
c=0
for j in range(len(l)):
    c =sum(l[j])
    print(c,end=" ")
    