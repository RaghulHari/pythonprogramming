import math
a=input()
a=a.split()
c=int(a[0])
d=int(a[1])
cc=0
for i in range(c,d+1):
    
    r=math.sqrt(i)
    if(r*r==i):
        cc=cc+1
print(cc)
