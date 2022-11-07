def prime(a):
    if a==1:
        return False
    for j in range(2,int(a**0.5)+1):
        if a%j==0:
            return False
    return True
a=int(input())
b=int(input())
d=0
for i in range(a,b+1):
    if prime(i):
        d+=1
print(d)