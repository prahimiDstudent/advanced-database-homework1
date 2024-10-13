#program to get n and then n number fromuser and compute maximum,minimum,average and standarddeviation
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
mean=sum(num)/count
j=1 
list2=[]
while j<=count:
     d=((num[j-1]-mean)**2)
     list2.append(d)
     j=j+1
stdev=math.sqrt(math.fsum(list2))/math.sqrt(count)
nummax=max(num)
print(f'maximum={nummax} ,  minimum={min(num)} , average={sum(num)/count} , standarddev={stdev} ')