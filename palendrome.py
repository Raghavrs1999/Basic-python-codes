rev=0
n=int(input("Enter the number: "))
num=n
while n>0:
    d=n%10
    n=n//10
    rev=d+rev*10
if num==rev:
    print("{} is palendrome number".format(num))
else:
    print("{} is not a palendrome number".format(num))