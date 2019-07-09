n=input()
n=n.split()
g=int(n[1])
d=input()
d=d.split()
w=len(d)
l=[]
v=0
for i in d:
    l.append(i)
for i in range(0,w):
    if(int(l[i])==g):
        print(i+1)

