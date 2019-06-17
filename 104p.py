n=int(input())
s=input()
s=s.split()
s=list(map(int,s))
print(s)
l=[]
for i in s:
    l.append(i)
s1=0

for i in range(0,n):
    k=i+1
    for j in range(k,n):
        s1=s1+l[i]+l[j]
        break
print(s1)
