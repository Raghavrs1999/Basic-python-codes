x=0
num=int(input("Enter the number: "))
for i in range(1,num):
    if num%i==0:
        x=x+i
if x==num:
    print("{} number is perfect number".format(num))
else:
    print("{} number is not perfect number".format(num))