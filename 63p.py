aa=int(input())
ff=input()
gg=input()
ff=ff.split()
gg=gg.split()
ff.sort()
gg.sort()
l=[]
m=[]
d=[]
for k in ff:
    l.append(k)
for h in gg:
    m.append(h)

for i in range(0,len(l)):
    if(l[i]==m[i]):
        d.append((l[i]))
print(*d,sep=" ")
        

