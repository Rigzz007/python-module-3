'''
1)how can you pick a random item from a list or tuple?
2)how can you pick a random item from a range?
*3)how can you get a random number in python?
'''
'''
import random
l=[1,15,42,78,46,19,43,5,64,95,82]
l1=random.choice(l)
print(l1)
'''
'''
import random
t=(1,15,42,78,46,19,43,5,64,95,82)
t1=random.choice(t)
print(t1)
'''
'''
import random
a=random.randint(0,100)
print(a)
'''
'''
from random import randrange
print(randrange(10))
'''