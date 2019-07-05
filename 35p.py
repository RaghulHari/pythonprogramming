n=input()

n=n.replace(" ","")
l=[]
for i in  n:
    if(n.count(i)==1):
        l.append(i)
print(*l,sep=" ")

