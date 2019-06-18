n=int(input())

s=input()
s=s.split()
s=list(map(int,s))
a=1
l=0
k=0
for i in range(0,n):
    a=a*s[i]

for i in range(2,a):
    k=0
    for j in range(0,n):
        if(i%s[j]==0):
            k=k+1
    if(k==n):
        print(i)
            
    
    
