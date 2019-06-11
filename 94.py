n=input()
mn=input()
n=n.split()
n=list(map(int,n))

mn=mn.split()
mn=list(map(int,mn))
a=int(n[1])

for i in mn:
    if(i==a):
        print(i)
        
