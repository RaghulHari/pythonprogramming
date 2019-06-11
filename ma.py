a=int(input())
b=list(map(int,raw_input().split()))
d=len(b)
b.sort()
j=0
for i in range(0,d):
    if(i!=d-1):
        if(b[i]==b[i+1]):
            print(b[i])

    
