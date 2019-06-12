j=input()
j=j.split()
c=0
aa=len(j)
l=[]
a=list(j[0])
m=list(j[1])
cc=int(j[2])

for i in range(0,aa):
    if(a[i]!=m[i]):
      c=c+1
      
if(c==cc):
    print("yes")
else:
    print("no")
      
