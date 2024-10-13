#program to get a number with exactly 5digits and find maximum digit use function and then use another function to delete maximum digit from  the number
def maximum(num):
     return (max(num))
     
def delmax(num,max1):
     b=num.translate({ord(max1):None})
     return(b) 
def inputnumber():
     number=(input('Enter a 5 digits number: '))
     if len(number)==5:
         return(number)
     else:
          inputnumber()
      
number1=inputnumber()
m=maximum(number1)
number2=delmax(number1,m)
print ("your number after delete maximum digit=",number2)