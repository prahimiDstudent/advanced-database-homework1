#program to print all 4digits numbers(between 1000,9999)that sum of first and second digits is equel with the product of the third and forth digits are
num=1000 
# Create an empty list to store our digits in. 
digits = []
print("numbers between 1000,9999 that sum of first and second digits is equel with the product of the third and forth digits are:")
while num<10000:
     x=num
     while x > 0:
         remainder = x % 100:4
         digits.append(remainder)
         x //= 10
# Reverse the list in-place to get the original order of the digits.
     digits.reverse()

     if((digits[0]+digits[1])==(digits[2]*digits[3])):
         print(f"  {digits[0:4]}")
     num=num+1