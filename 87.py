aa=input()
aa=aa.split()
cc=int(aa[0])
dd=int(aa[1])
i=1
while(i<=cc and i<=dd):
    if(cc%i==0 and dd%i==0):
        gcd=i
    i=i+1
print(gcd)
