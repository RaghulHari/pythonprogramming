hh=input()
hh=hh.split()
g=[]
for i in hh:
    g.append(i[::-1])
print(*g,sep=' ')
