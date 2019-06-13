nn=int(input())
if(nn>-2**15+1 and nn<2**15+1):
    print("INT")
elif(nn>-2**31+1 and nn<2**31+1):
    print("LONG")
else:
    print("invaild")

