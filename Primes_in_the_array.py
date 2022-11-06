def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    return False

n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    if prime(i):
        d+=1
print(d)