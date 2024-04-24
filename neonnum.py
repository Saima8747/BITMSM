sum=0
num=int(input('enter number'))
sq=num*num
while(sq!=0):
    digit=sq%10
    sum=sum+digit
    sq=sq//10
if(num==sum):
    print(num,'is a neon number')
else:
    print(num,'not a neon number')