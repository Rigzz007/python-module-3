'''
1)write a python program to return sum of all divisors of a number
2)write a python program to find the maximun and minimum numbers from the specified decimal numbers.
'''
#1)

n=int(input("Enter the number:"))
d=[1]

for i in range(2,n):
    if (n%i)==0:
       d.append(i)
print(d)
sum=sum(d)
print(sum)

'''
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))
'''
#2)

l=[2.45, 2.69, 2.45, 3.45, 2.00 ,0.04 ,7.25]
print(max(l))
print(min(l))

'''
from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))
'''