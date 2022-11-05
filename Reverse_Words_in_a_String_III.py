def rev(a):
    return a[::-1]


n=input()
s=[]
l=list(n.split(" "))
for i in l:
    s.append(rev(str(i)))
print(*s)