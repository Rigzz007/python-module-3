'''
write a python program to create and diplay all combinations of letters,selecting each letter from a different key in a dictionary.
sample data:{'1':['a','b'],'2':['c','d']}
expected output: ac ad bc bd
'''
d={'1':['a','b'],'2':['c','d']}

'''
data = {'1':['a','b'], '2':['c','d']}

for i in range(len(data["1"])):
    for j in range(len(data["2"])):
        print(data["1"][i]+data["2"][j])
'''
'''
sample = {'1':['a','b'], '2':['c','d']}
list_1 = sample['1']
list_2 = sample['2']
for i in list_1:
    for j in list_2:
        result = i + j
        print(result)
'''
'''
#An updated answer using list comprehension. The end result will be in a list. This is shorter and more "pythonic".
sample = {'1':['a','b'], '2':['c','d']}
result = [i+j for i in sample["1"] for j in sample["2"]]
print(result)

'''
'''
d={'1':['a','b'], '2':['c','d']}

L1,L2=d.values()
for x in L1:
    for y in L2:
        print(x+y)

'''
'''
sample={'1':['a','b'], '2':['c','d']}
for i in sample['1']:
    for j in sample['2']:
        result=i+j
        print(result)
'''
'''
data = {'1':['a','b'], '2':['c','d']}
a,b = data.values()

#print(a)
for i in a:
    for j in b:
        print(i+j)
'''
'''
dic = {'1':['a','b'], '2':['c','d']}
l1 = dic['1']
l2 = dic['2']
for i in l1:
    for j in l2:
        print(i+j)
'''
'''
#
for x in d['1']:
    for y in d['2']:
        print(x + y)
'''#
'''
my_dict= {'1':['a', 'b'], '2':['c', 'd'}}
my_list= list(my_dict.values())
for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)
'''
'''
import itertools
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
'''
