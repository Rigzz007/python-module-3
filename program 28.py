'''
write a python script to sort (ascending and discending) a dictionary by value.
'''
'''
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
'''
'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d.items()))
print(sorted(d.items(),key=lambda x:x[1]))
print(sorted(d.items(),reverse=True))
print(sorted(d.items(),key=lambda x:x[1],reverse=True ))
'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d1=sorted((value,key))
print(d1)