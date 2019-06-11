import math
nkl=input()
nkl=nkl.split()
n=int(nkl[0])
m=int(nkl[1])
y=int(nkl[2])
ee=(n*m)//y
print(math.ceil(ee))
