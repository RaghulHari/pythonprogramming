aa=input()
bb=input()
aa=aa.split()
bb=bb.split()
cc=int(aa[1])
oo=len(bb)

l=[]
m=[]
for i in bb:
    l.append(i)

for i in range(0,oo):
    if(int(l[i])<cc):
        m.append(l[i])
m.sort()
print(*m,sep=" ")

