aa=int(input())
bb=input()

bb=bb.split()

oo=len(bb)

l=[]
m=[]
for i in bb:
    l.append(i)

for i in range(0,oo):
    if(int(l[i])<aa):
        m.append(l[i])
print(*m,sep=" ")


