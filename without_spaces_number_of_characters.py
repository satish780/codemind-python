def space(a):
    c=0
    for i in a:
        c+=1
    return int(c)

n=input()
l=list(n.split(" "))
d=0
for i in l:
    d+=space(i)
print(d)
