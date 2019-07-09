n=int(input())
d=input()
d=d.split()
l=[]
for i in d:
  l.append(i)
m=[]
m.append(l[0])
c=int(l[0])
for i in range(0,n-1):
  c=c+int(l[i+1])
  m.append(c)
f=m
d=m[::-1]
j=[]
for i in range(0,n):
  g=int(f[i])+int(d[i])
  j.append(g)
print(*j,sep=" ")
