n=int(input())
fto=1
if(n==0):
    print("1")
elif(n<=1):
    print("1")
else:
    for i in range(1,n+1):
        fto=fto*i
    print(fto)
