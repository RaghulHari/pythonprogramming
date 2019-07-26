n=int(input())
m=input()
m=m.split()
l=[]
s1=[]
s=[]
for i in m:
    l.append(i)
for i in m:
    if(l.count(i)==1):
        s.append(i)
    else:
        s1.append(i)
d=set(s)
f=sorted(d)
v=list(f)
print(*v,sep="")

        
