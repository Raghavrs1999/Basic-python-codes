start=int(input("Enter the number for where have to start: "))
end=int(input("Enter the number where have to end:"))
if start<end:
    for i in range (start,end+1):
        print(i)
elif start>end:
    for i in range (start,end-1,-1):
        print(i)