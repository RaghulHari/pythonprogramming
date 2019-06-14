a=int(input())
c=input()
c=c.split()
c=list(map(int,c))

c.sort()
d=c[0]
e=c[1]
f=e-d
print(f)
