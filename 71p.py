n=int(input())
d=input()
d=d.split()
l=[]
m=[]
for i in d:
    l.append(i)
for i in range(0,n-1):
    if(l[i]>l[i+1]):
        m.append(l[i])
    else:
        m.append(l[i+1])
print(*m,sep=" ")
