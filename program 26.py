'''
write a python program to convert a list of tuples into dictionary.
'''

t=[(1,"rignesh"),(2,"ankit"),(3,"arth")]
d=dict(t)
print(d)
'''
def Convert(tup, dic):
    for a, b in tup:     # iterating over the tuples lists
        dic.setdefault(a, []).append(b)        # setting the default value as list([]) appending the current value
    return dic

tups = [("RIGNESH", 19), ("ANKIT", 19), ("ARTH", 16)]
dictionary = {}
print (Convert(tups, dictionary))
'''
