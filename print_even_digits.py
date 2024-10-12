
# Online Python - IDE, Editor, Compiler, Interpreter
even_digits=""
num1 = input('Enter your number: ')
for i in range(len(num1)):
    if(int(num1[i]) % 2)==0:
      even_digits+=f'{num1[i]} *'
   
print(even_digits)


