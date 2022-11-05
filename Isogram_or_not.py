n=input()
n=n.lower()
c=0
s=set(n)
for i in n:
    if i in s:
        c+=1
if c==len(s):
    print(True)
else:
    print(False)