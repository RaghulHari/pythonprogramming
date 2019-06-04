n=input()
n=n.split()
m=input()
m=m.split()

l=[]
h=[]
for i in n:
    l.append(int(i))
    

for j in m:
    h.append(int(j))

c=0
k=int(n[1])
t=int(n[0])

if(k<=t):
    for i in range(0,k):
        c=c+int(h[i])
print(c)
