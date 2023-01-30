'''
write a python program to select an item randomly from a list.
'''
#complete

import random
l=[1,2,5,48,15,96,78,16,49,48,46,26,72,3,4,86,99,76,68]
l2=[]
for i in range(5):
    a=random.choice(l)
    l2.append(a)
print(l2)
