n=int(input())
ss=input()
ss=ss.split()
ss=list(map(int,ss))

l=[]
for i in ss:
    l.append(i)
s1=0

for i in range(0,n):
    k=i+1
    for j in range(k,n):
        s1=s1+l[i]+l[j]
        break
print(s1)
