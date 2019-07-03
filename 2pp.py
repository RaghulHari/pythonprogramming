n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
c=0
for j in range(a,b+1):
    for i in range(2,j):
        if(j%i==0):
            break
    else:
        c=c+1
print(c)
    
