n=int(input())
ft=1
if(n==0):
    print("Invalid")
elif(n<=1):
    print("1")
else:
    for i in range(1,n+1):
        ft=ft*i
    print(ft)
