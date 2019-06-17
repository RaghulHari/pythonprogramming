n=int(input())
s=list(map(int,input().split()))

l=[]
for i in s:
    l.append(i)
s1=0
for i in range(1,n):
    s1=s1+l[i]
print(s1)
    
