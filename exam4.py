#program to print all 3 digits numbers(between100,999)that does not have odd digits
num=100 
# Create an empty list to store our digits in. 
digits = []

print(f"numbers(between100,999)that does not have odd digits")
while num<999:
     x=num
     while x > 0:
         remainder = x % 10
         digits.append(remainder)
         x //= 10
     


# Reverse the list in-place to get the original order of the digits.
     digits.reverse()

     if((digits[0]%2)==(digits[1]%2)==(digits[2]%2)==0):
         print(digits[0:3])
     num=num+1