flag = 0
num =int(input("Enter the Number: "))

for i in range (2,num):
    if num % i == 0:
        flag+=1
    if flag == 1:
        break

if flag == 1:
    print("Given number is not prime")
elif flag ==0:
    print("Given number is prime")
        