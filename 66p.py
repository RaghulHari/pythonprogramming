ff=input()
ff=ff.split()
aa=input()
aa=aa.split()
aa=list(map(int,aa))
cc=int(ff[1])
dd=len(aa)
for i in aa:
    if aa.count(i)==cc:
        print(i)
        break
        
