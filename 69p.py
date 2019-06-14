nn=input()
nn=nn.split()
ss=int(nn[1])
aa=input()
aa=aa.split()
l=[]
for i in aa:
    l.append(i)
for i in range(0,ss):
    l.pop()
print(*l,sep=" ")
