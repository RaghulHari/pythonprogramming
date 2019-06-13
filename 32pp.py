n=input()
n=n.split()
d=int(n[1])
m=input()
m=m.split()
m.sort()

g=len(m)


for i in range(0,g):
    if(m[i]==str(d) ):
        print("Yes")
    else:
        print("No")
        
