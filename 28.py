a=int(input())
m=input()
m=m.split()
m=list(map(int,m))
for i in range(0,len(m)):
    print(m[i],' ',i)

