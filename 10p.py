n=input()
n=n.split()
a=list(n[0])
b=list(n[1])
c=0
for i in range(0,len(a)):
    if(a[i]==b[i]):
        c=c+1
        
if(c==len(a)-1):
    print("yes")
else:
    print("no")
