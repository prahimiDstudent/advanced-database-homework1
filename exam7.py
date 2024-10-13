#write program to define 4function to calculate min, max,average , std . min, max return result but average andstd print result in their own  body
import math
import numpy
from array import array 
num=array('i')
i=0
number=0
count=int(input('Enter the count of numbers: '))
for i in range(0,count):
     number=int(input(f'enter number {(i+1)}:'))
     num.append(number)

def maximum(num):
     return max(num)
     
def minimum(num):
     return min(num)
     
def average(num,n):
     print(f'the average is:{sum(num)/n}')
     return()
     
def standarddeviation(num,n):
     mean=sum(num)/n
     j=1 
     list2=[]
     while j<=count:
          d=float(((num[j-1]-mean)**2))
          
          list2.append(d)
  #        print(list2)
          j=j+1
     stdev=math.sqrt(math.fsum(list2))/math.sqrt(count)
     print(f'standarddeviation= {stdev}')
     return 


print(f'maximum={maximum(num)} ,  minimum={minimum(num)} ')
average(num,count)
standarddeviation(num,count)