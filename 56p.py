ny=input()
ny=ny.split()
a=ny[0]
b=ny[1]
for i in a:
    if(i==b):
        print(a.index(i)+1)
        break

