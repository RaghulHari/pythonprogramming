j=int(input())
if(j>1):
    for i in range(2,j//2):
        if(j%i==0):
            print("no")
            break
    else:
        print("yes")
