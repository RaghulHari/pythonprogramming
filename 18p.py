n=int(input())
c=0
a=[]
b=['a','a','b','i','k','l']
for i in range(0,n):
    a.append(list(input()))
for i in a:
    s=sorted(i)
    if(b==s):
        c=c+1
print(c)
        
