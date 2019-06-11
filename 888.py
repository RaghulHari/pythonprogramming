num1=input()
num1=num1.split()
a=int(num1[0])
b=int(num1[1])
lcm=0
if a>b:
    greater=a
else:
    greater=b
while(True):
    if((greater%a==0) and(greater%b==0)):
        lcm=greater
        break
    greater+=1
print(lcm)
