nn=input()
nn=nn.split()

a=list(nn[0])
b=list(nn[1])
for i in range(0,len(a)):
    if(a[i]==b[i]):
        print("yes")
        break
    else:
        print("no")
        break
