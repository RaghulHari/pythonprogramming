n=int(input())
l=[]
k=0
for i in range(2,n):
    d=0
    if(n%i==0):
        for j in range(2,i):
            k=0
            if(i%j==0 and i!=j):
                k=1
                break
        if(k!=1):
            l.append(i)
print(*l,sep=" ")
