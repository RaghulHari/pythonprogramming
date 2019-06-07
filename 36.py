n=input()
c=0
m=len(n)
for i in range(0,m):
    
    if(n[i].isdigit()):
       c=c+1
    if(n[i].isalpha()):
       c=c+1

f=m-c
print(f)
