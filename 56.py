n=input()
d=0
c=0
for i in n:
    if(i.isnumeric())==True:
        c=1
    elif(i.isalpha())==True:
        d=1
if(c==1 and d==1):
    print("Yes")
else:
    print("No")
    
