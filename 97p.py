f=input()
f=f.split()
a=int(f[0])
b=int(f[1])
l=[]

for i in range(a,b+1):
    if(i%2!=0):
        l.append(i)
print(sum(l))
    
