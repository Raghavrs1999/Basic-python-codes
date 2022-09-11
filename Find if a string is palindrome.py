s = input("Enter string: ")
l = len(s)
flag = 0
r=l//2
for i in range(0,r):
    if s[i]==s[l-1-i]:
        continue
    else:
        flag=1
if flag == 0:
    print("String is palindrome")
else:
    print("String is not palindrome")