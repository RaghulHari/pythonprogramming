ad=input().split()
af=ad[0]
ax=ad[1]
af=list(af)
ax=list(ax)
h=0
d=af[0]
c=ax[0]
j=0
for i in range(0,len(af)):
        if(af[i]==d and ax[j]==c):
            h=h+1
        elif(af[i]!=d and ax[j]==c):
            break
        elif(af[i]==d and ax[j]!=c):
            break
        elif(af[i]!=d and ax[j]!=c):
            d=af[i]
            c=ax[j]
            h=h+1
        j=j+1
if(h==len(ax)):
    print("yes")
else:
    print("no")
