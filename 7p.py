aa=input()

aa=list(aa)

l=[]
for i in range(0,len(aa)):
    if(i%2==0):
        l.append(aa[i+1])
    elif(i%2==1):
        l.append(aa[i-1])
print(*l,sep="")

