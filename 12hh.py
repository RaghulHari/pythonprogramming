a=input()
a=a.split()
b=input()
b=b.split()

c1=int(a[1])
b=list(map(int,b))
c=sorted(b)
d=c[::-1]
f=str(d)
f=d[c1-1]
print(f)
