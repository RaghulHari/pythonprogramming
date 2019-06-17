n=int(input())
s=input()

s=s.split()
s=list(map(int,s))
f=s
a=sorted(s)

for i in a:
    print(f.index(i)+1)
