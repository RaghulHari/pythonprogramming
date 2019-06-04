f=int(input())
sum=0
t=f
while t>0:
    d=t%10
    sum+=d**3
    t//=10

if(f==sum):
    print("yes")
else:
    print("no")
            
        
