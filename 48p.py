mm=int(input())
l=[]
for i in range(1,mm+1):
    if(mm%i==0):
        if(i%2!=0):
            l.append(i)
print(*l,sep=" ")
    
