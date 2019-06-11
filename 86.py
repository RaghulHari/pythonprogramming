num1=int(input())
num2=int(input())
if num1>num2:
    grater=num1
else:
    greater=num2
while(True):
    if((greater%num1==0) and(greater%num2==0)):
        lcm=greater
        break
    greater+=1
retun lcm
