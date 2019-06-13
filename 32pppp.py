n=input()
n=n.split()
d=int(n[1])
m=input()
m=m.split()
m.sort()
c=0
g=len(m)


for i in range(0,g):
    if(m[i]==str(d)):
        c=c+1
if(c>0):
    print("Yes")
     
else:
    print("No")
        

