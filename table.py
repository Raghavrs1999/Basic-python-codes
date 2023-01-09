num = int (input ("Enter the number:"))
for i in range(1,11):
    print("{} * {} = {}".format(num ,i , i*num))
    
    
# table between two number


start = int (input ("Enter the starting number: "))
end = int (input ("Enter the range of number:"))
for j in range(start, end+1):
    print()
    for i in range(1,11):
        print("{} * {} = {}".format(j ,i , j*i))