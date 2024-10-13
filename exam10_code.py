#program to compute factorial of 4 
def factorial(x):
    if x == 1:# this is the base case
        return 1;
    else:# this is the recursive case
        return (x*factorial(x-1));

print(factorial(4));