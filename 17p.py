a=input()
a=a.split()
a=list(map(int,a))
bb=int(a[0])
cc=int(a[1])
for ii in range(1,bb*cc+1):
    if(ii%bb==0)and(ii%cc==0):
        print(ii)
        break
