n=input()
c=v=d=0
l=list(n.split(" "))
ws=len(l)-1
s="aeiou"
for i in n:
    if i in s:
        v+=1
    elif i.isdigit():
        d+=1
    else:
        c+=1
        
print("Vowels: {}".format(v))
print("Consonants: {}".format(c-ws))
print("Digits: {}".format(d))
print("White spaces: {}".format(ws))