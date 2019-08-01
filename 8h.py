n=int(input())
m=input()
m=m.split()
l=[]
t=0
l3=[]
for i in m:
    l.append(int(i))
for i in range(0,len(m)-1):
    for j in range(1,len(m)):
        t=l[i]+l[j]
        if t in l:
            print(l[i],l[j],t)
