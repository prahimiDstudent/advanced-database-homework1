#program to get n from user and print pattern
i=1
j=1
num1 =input('Enter your number: ')
print("your pattern is:")
while i<=int(num1):
     j=1
     while j <= i:
         print(f"{(i*j)}", end=" ")
         j=j+1
     i=i+1
     print()
