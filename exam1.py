#program to get a number and print all its even digits seperated by*
even_digits=[]
num1 = input('Enter your number: ')
for i in num1:
     i=int(i)
     if i % 2==0:
      even_digits.append(str(i))
print("  even digits of your number are:") 
print("*". join(even_digits))

