n=input()
n=n.split()
l=[]
m=[]
c=[]
for i in n:
    l.append(int(i))
k=int(l[0])
t=int(l[1])
if(k<t):
    for i in range(k+1,t):
        if(i%2!=0):
            m.append(str(i))
c=' '.join(m)
print(c)
