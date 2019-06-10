hh=int(input())
l=[]
for i in range(1,hh+1):
    if(hh%i==0):
        l.append(i)
print(*l,sep=" ")
