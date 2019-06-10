l=input()
j=[]
for i in l:
    if(int(i)%2!=0):
        j.append(i)
print(*j,sep=" ")
