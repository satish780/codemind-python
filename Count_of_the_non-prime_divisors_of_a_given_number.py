def prime(a):
    c=0
    for j in range(1,a+1):
        if a%j==0:
            c+=1
    if c!=2:
        return True
    return False
    
a=int(input())
d=0
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            d+=1
print(d)