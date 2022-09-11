itr = int(input("Enter numbers of iteration: "))
a=0
b=1
c=0
for i in range(0,itr):
    print(c,end=(" "))
    c=a+b
    a=b
    b=c