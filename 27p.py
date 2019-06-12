a=input()
a=list(a)

newstr=""
for i in range(0,len(a)):
    if(a[i].islower())==True:
        newstr+=a[i].upper()
    elif(a[i].isupper())==True:
        newstr+=a[i].lower()
    else:
        newstr+=a[i].lower()
print(newstr)

