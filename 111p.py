n=input()
n=n.split()
k=input()
k=k.split()
a=int(n[0])
b=int(n[1])
c=0
c=a+b

l=[]
m=[]
d=[]
g=[]
for i in k:
    l.append(i)
for i in range(0,a):
    m.append(l[i])
for i in range(a,c):
    d.append(l[i])
for i in range(0,a):
    for j in range(0,b):
        if(m[i]==d[j]):
            g.append(m[i])
print(*g,sep=" ")

