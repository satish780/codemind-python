n=input()
c=0
for i in n:
    if n.count(i)==1:
        c+=1
        break
if c==1:
    print(n.index(i))
else:
    print(-1)