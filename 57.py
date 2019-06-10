n=input()
m=input()
n=n.split()
m=m.split()
u=int(n[1])
c=1
for i in m:
    if(i==u):
        c=c+1
print(c)
    
