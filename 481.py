n=int(input())
c=input()
c=c.split()
d=0
e=0
c=list(map(int,c))
for i in c:
    d=d+i
    e=d//n
print(e)
    
