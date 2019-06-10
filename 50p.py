kk=int(input())
z=x=0
for i in range(1,kk):
    x=0
    p=2**i
    if s==p:
        print("yes")
        exit()
        x=1
    else:
        z=1
if(x!=1):
    print("no")
