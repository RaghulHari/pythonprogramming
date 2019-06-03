f=input()
f=f.split(" ")
l=[]
for i in f:
    l.append(int(i))
if(l[0]>l[1] and l[0]>l[2]):
    print(l[0])
elif(l[1]>l[0] and l[1]>l[2]):
    print(l[1])
else:
    print(l[2])


