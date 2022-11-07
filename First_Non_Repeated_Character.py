t=int(input())
for i in range(t):
    a=int(input())
    n=input()
    c=0
    for i in n:
        if n.count(i)==1:
            c+=1
            print(i)
            break
    if c==0:
        print(-1)