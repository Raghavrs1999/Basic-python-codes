s = input("Enter the string: ")
c=0
for i in s:
    if i=="a" or i=="A":
        c+=1
    elif i=="e" or i=="E":
        c+=1
    elif i=="i" or i=="I":
        c+=1
    elif i=="U" or i=="U":
        c+=1
print("There are {} vowels in string".format(c))