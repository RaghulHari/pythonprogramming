x=list(input())
v=len(x)
for i in range(len(x)):
    if v%2==0:
        if i==v//2-1 or i==v//2:
            print('*',end='')
        else:
            print(x[i],end='')
    else:
        if i==v//2:
            print('*',end='')
        else:
            print(x[i],end='')
