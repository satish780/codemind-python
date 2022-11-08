def lst(a):
    return a[0]

n=input()
l=list(n.split())
a=l[::-1]
for i in a:
    print(lst(i))
    break
