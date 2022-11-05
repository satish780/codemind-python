a=input()
b=input()
l=a.lower()
m=b.lower()
x=list(l.split(" "))
y=list(m.split(" "))
for i in y:
    if i in x:
        print(i,end=" ")