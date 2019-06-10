n=input()
n=n.split()
n=list(map(int,n))
a=int(n[0])
b=int(n[1])
l=[]
for i in range(a,b+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                
                break
        else:
            l.append(i)
print(*l,sep=" ")
