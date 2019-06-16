s=input()
c=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            c=1
            break
if c==1:
    print("yes")
else:
    print("no")
    
