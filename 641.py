e=input()
e=e.split()
e=list(map(int,e))
a=e[0]
b=e[1]
c=a+b
if(c%2==0):
    print("even")
else:
    print("odd")
