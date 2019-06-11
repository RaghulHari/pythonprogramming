pp=input()
l=[]
for i in pp:
    if(i.isdigit())==True:
        l.append(i)
print(*l,sep="")
