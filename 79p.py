a=int(input())
c=input()
c=c.split()
c=list(map(int,c))

c.sort()
d=min(c)
f=max(c)
p=f-d
print(p)

