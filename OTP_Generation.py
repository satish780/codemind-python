n=input()
l=[]
for i in n:
    if int(i)%2==0:
        continue
    else:
        l.append(int(i)**2)
for i in l:
    print(i,end="")