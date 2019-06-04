a=input()
a=a.split()
l=[]
for i in a:
    l.append(int(i))
n=int(l[0])
m=int(l[1])
for num in range(n,m+1):
    order=len(str(num))
    s=0
    temp=num
    while(temp>0):
        d=temp%10
        s+=d**order
        temp//=10
    if(num==s):
        print(num)
    

