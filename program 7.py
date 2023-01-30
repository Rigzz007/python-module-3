'''
write a python program to generate and print a list of first and last 5 element where the values are square of numbers between 1 and 30.
'''
#complete
'''
l=[]
for i in range(1,31):
    l.append(i*i)
print(l[0:5]+l[-5:])
'''

import random
l1=[]
l2=[]
for i in range(10):
    a=random.randint(0,31)
    l1.append(a)
    l2.append(a*a)

print(l1)
print(l2)


