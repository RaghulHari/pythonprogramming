nm=int(input())
s=input()
s=s.split()
s=list(map(int,s))
l=[]


m=[]
for i in range(nm):
    if(s[i]==i):
        m.append(i)
        
l3=sorted(m)
if(len(l3)==0):
    print("-1")
else:
    print(*l3,sep=" ")
