n=input()
n=n.split()
m=input()
m=m.split()
y=input()
y=y.split()
count=0
for i in m:
    if i in y:
        count=count+1
if(count==len(y)):
    print("YES")
else:
    print("NO")
