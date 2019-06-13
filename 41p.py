n=input()
n=n.split()
m=int(n[0])
k=int(n[1])
i=1
c=0
while(i!=m):
    i=i*k
    if(i>m):
        break
if(i==m):
    print("yes")
else:
    print("no")
      
