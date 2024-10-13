#program to compute expression for 500 sentences but this program can calculate for 11 sentences!
import math
from array import array 

result=array('d')
first = 3
second = 2
third =9
sign=1

for i in range(0,11):
     result1 =sign*(math.factorial(first))/(second+third)
     result.append(result1)
     first=first+2
     second=second+1
     third=third-2
     sign=sign*-1
print(f"The sentances are: {result}")
print(f"The calculate of 11 sentences is {sum(result)}")
