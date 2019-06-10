x=input()
l=list(map(int,x))
for i in l:
    if(i==0 or i==1):
        c=1
    else:
        c=0
if(c==1):
    print("yes")
else:
    print("no")
        
