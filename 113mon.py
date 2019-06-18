l=input()
l=l.split("/")
a=l[0]
b=l[1]
c=l[1]
e=len(a)

f=len(b)
g=len(c)


if e==2 and f==2 and g==4 and int(l[0])>0 and int(l[0])<32 and int(l[1])>=1 and int(l[1])<13:
    print("yes")
else:
    print("no")
