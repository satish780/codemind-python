def v_cnt(a):
    c=0
    s="aeiou"
    for i in a:
        if i in s:
            c+=1
    return c
n=input()
m=n.lower()
d=0
l=list(m.split(" "))
s=[]
for i in l:
    s.append(v_cnt(i))
d=min(s)
print(d)

    