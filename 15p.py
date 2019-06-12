n=input()
n=list(n)
c=len(n)
l=[]
h=[]
count=0
for i in n:
    l.append(i)
for i in range(0,c):
    k=i+1
    for j in range(k,c):
        if(l[i]==l[j]):
            h.append(l[i])
h=list(h)
a=h[::-1]
b=a[0]
print(b)



