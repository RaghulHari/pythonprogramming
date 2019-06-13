n=int(input())
m=input()
m=m.split()
a=len(m)
l=[]
for i in m:
    l.append(i)
m.sort()
if(l==m):
    print("yes")
else:
    print("no")

