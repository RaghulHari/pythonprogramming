s=input()
s=s.split("-")
a=s[0]
b=s[1]
c=s[2]
aa=len(a)
bb=len(b)
cc=len(c)
dict={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
if(aa==2 and bb==2 and cc==4 and int(s[0])>0 and int(s[0])<31 and int(s[1])>=1 and int(s[1])<13):
    print(dict[b])
    
   
