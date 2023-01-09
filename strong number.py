x=0;f=1
num=input("Enter the number: ")
for i in num:
    i=int(i)
    for n in range(i,0,-1):
        f=f*n
    x=x+f
    f=1
num=int(num)
if x==num:
    print("{} is strong number ".format(x))
else:
    print("{} is not a strong number".format(num))