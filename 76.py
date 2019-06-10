ll=int(input())
c=0
if(ll>1):
    for i in range(2,ll//2):
        if(ll%i==0):
            print("yes")
            break
else:
    print("no")
            
