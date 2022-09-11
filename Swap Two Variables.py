a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("First number: {}\nSecond number: {}".format(a,b))