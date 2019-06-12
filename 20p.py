n=input()
l=[]
n=list(n)
for i in n:
    if(ord(i)>=65):
        c=ord(i)+3
    l.append(chr(c))
print(*l,sep="")
    
