f = 1
fact = int (input("Enter the number: "))
for i in range(1,fact+1):
    f = i * f
print("Factorial of {} is {}".format(fact,f))