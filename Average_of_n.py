l=[]
r = int(input("Enter the range of numbers:"))
for i in range(0,r):
    num=int(input("Enter the number:"))
    l.append(num)
print("These are the numbers",l)
total=0
for i in l:
    total=total+i
avg=total/r
print("Average value is ",avg)