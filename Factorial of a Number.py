num = int(input("Enter number: "))
fact = 1

for i in range(2,num+1):
    fact = i*fact
    
print("Factorial of {} is {}".format(num,fact))