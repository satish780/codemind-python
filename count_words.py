def vow(a):
    s="AEIOUaeiou"
    c=0
    if (a[0] in s) and (a[-1] not in s):
        c+=1
    return c
        
            

n=input()
a=0
l=list(n.split(" "))
for i in l:
    a+=vow(i)
print(a)
    
