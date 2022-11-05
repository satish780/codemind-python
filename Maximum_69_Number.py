n=input()
l=[]
for i in n:
    l.append(int(i))
for i in range(len(n)):
    if l[i]==6:
        l[i]=9
        break
s=''
for i in l:
    s +=str(i)
print(int(s))